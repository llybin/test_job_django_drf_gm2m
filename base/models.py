from functools import reduce

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title


content_type_limit = reduce(
    lambda a, b: a | b,
    [
        models.Q(app_label='base', model='text'),
        models.Q(app_label='base', model='video'),
    ],
    models.Q(app_label='base', model='audio')
)


class PageContent(models.Model):
    page = models.ForeignKey(Page, related_name='content', on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=content_type_limit,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey('content_type', 'object_id')

    order = models.PositiveIntegerField()

    class Meta:
        ordering = ('-order',)


class ContentMixin(models.Model):
    counter = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Audio(ContentMixin):
    audio = models.FileField(upload_to='audio/')
    bitrate = models.PositiveIntegerField()


class Text(ContentMixin):
    text = models.TextField()


class Video(ContentMixin):
    video = models.FileField(upload_to='video/')
    subtitles = models.FileField(upload_to='subtitles/', blank=True)
