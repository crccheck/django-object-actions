from django.contrib import admin
from django.core.urlresolvers import reverse
from django.db.models import F
from django.http import HttpResponseRedirect

from django_object_actions import (DjangoObjectActions,
        takes_instance_or_queryset)

from .models import Choice, Poll


class ChoiceAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('poll', 'choice_text', 'votes')

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

    def decrement_vote(self, request, obj):
        obj.votes -= 1
        obj.save()
    decrement_vote.short_description = "-1"

    def reset_vote(self, request, obj):
        obj.votes = 0
        obj.save()
    reset_vote.short_description = "0"

    def edit_poll(self, request, obj):
        url = reverse('admin:polls_poll_change', args=(obj.poll.pk,))
        return HttpResponseRedirect(url)

    objectactions = ('increment_vote', 'decrement_vote', 'reset_vote',
        'edit_poll')
    actions = ['increment_vote']

admin.site.register(Choice, ChoiceAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class PollAdmin(DjangoObjectActions, admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

    def delete_all_choices(self, request, obj):
        from django.shortcuts import render_to_response
        from django.template import RequestContext

        if request.method == 'POST':
            obj.choice_set.all().delete()
            return

        return render_to_response('clear_choices.html',
            dict(object=obj), context_instance=RequestContext(request))
    delete_all_choices.label = "Delete All Choices"

    objectactions = ('delete_all_choices', )


admin.site.register(Poll, PollAdmin)
