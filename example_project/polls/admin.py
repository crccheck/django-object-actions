from django.contrib import admin

from django_object_actions import DjangoObjectActions

from .models import Choice, Poll


class ChoiceAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('poll', 'choice_text', 'votes')

    def increment_vote(self, request, obj):
        print obj
        obj.votes += 1
        obj.save()
    increment_vote.short_description = "hi"

    objectactions = ('increment_vote', )

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

admin.site.register(Poll, PollAdmin)
