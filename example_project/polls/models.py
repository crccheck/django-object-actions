import datetime
from uuid import uuid4

from django.db import models
from django.utils import timezone


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comment or ""


class RelatedData(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    extra_data = models.TextField(blank=True, default="")

    def __str__(self):
        return self.extra_data or self.id
