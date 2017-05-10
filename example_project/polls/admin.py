from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse  # < django 1.10

from django_object_actions import (
    DjangoObjectActions, takes_instance_or_queryset)

from .models import Choice, Poll, Comment


class ChoiceAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('poll', 'choice_text', 'votes')

    # Actions
    #########

    @takes_instance_or_queryset
    def increment_vote(self, request, queryset):
        queryset.update(votes=F('votes') + 1)
    increment_vote.short_description = "+1"
    increment_vote.label = "vote++"
    increment_vote.attrs = {
        'test': '"foo&bar"',
        'Robert': '"); DROP TABLE Students; ',  # 327
        'class': 'addlink',
    }

    actions = ['increment_vote']

    # Object actions
    ################

    def decrement_vote(self, request, obj):
        obj.votes -= 1
        obj.save()
    decrement_vote.short_description = "-1"

    def delete_all(self, request, queryset):
        self.message_user(request, 'just kidding!')

    def reset_vote(self, request, obj):
        obj.votes = 0
        obj.save()
    reset_vote.short_description = "0"

    def edit_poll(self, request, obj):
        url = reverse('admin:polls_poll_change', args=(obj.poll.pk,))
        return HttpResponseRedirect(url)

    def raise_key_error(self, request, obj):
        raise KeyError

    change_actions = (
        'increment_vote', 'decrement_vote', 'reset_vote', 'edit_poll',
        'raise_key_error',
    )
    changelist_actions = ('delete_all',)
admin.site.register(Choice, ChoiceAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class PollAdmin(DjangoObjectActions, admin.ModelAdmin):
    # List
    ######

    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

    def changelist_view(self, request, extra_context=None):
        extra_context = {'foo': 'changelist_view'}
        return super(PollAdmin, self).changelist_view(request, extra_context)

    # Detail
    ########

    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information',
         {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra = {'foo': 'change_view'}
        return super(PollAdmin, self).change_view(request, object_id, form_url, extra)

    # Object actions
    ################

    def delete_all_choices(self, request, obj):
        from django.shortcuts import render

        if request.method == 'POST':
            obj.choice_set.all().delete()
            return

        self.message_user(request, 'All choices deleted')
        return render(request, 'clear_choices.html', {'object': obj})
    delete_all_choices.label = "Delete All Choices"

    def question_mark(self, request, obj):
        """Add a question mark."""
        obj.question = obj.question + '?'
        obj.save()

    change_actions = ('delete_all_choices', 'question_mark')

    def get_change_actions(self, request, object_id, form_url):
        actions = super(PollAdmin, self).get_change_actions(request, object_id, form_url)
        actions = list(actions)
        if not request.user.is_superuser:
            return []

        obj = self.model.objects.get(pk=object_id)
        if obj.question.endswith('?'):
            actions.remove('question_mark')

        return actions
admin.site.register(Poll, PollAdmin)


class CommentAdmin(DjangoObjectActions, admin.ModelAdmin):

    # Object actions
    ################

    def hodor(self, request, obj):
        if not obj.comment:
            # bail because we need a comment
            return
        obj.comment = ' '.join(['hodor' for x in obj.comment.split()])
        obj.save()
    change_actions = ('hodor', )
admin.site.register(Comment, CommentAdmin)


support_admin = AdminSite(name='support')
support_admin.register(Poll, PollAdmin)
