from rest_framework import serializers

from base.models import Page, Audio, Video, Text
from api.v1.tasks import increase_content_counter


class PagesSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:v1:pages-detail')

    class Meta:
        model = Page
        fields = (
            'id',
            'url',
            'title',
            'created_at',
            'modified_at',
        )


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = (
            'id',
            'counter',
            'title',
            'audio',
            'bitrate',
            'created_at',
            'modified_at',
        )


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id',
            'counter',
            'title',
            'video',
            'subtitles',
            'created_at',
            'modified_at',
        )


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = (
            'id',
            'counter',
            'title',
            'text',
            'created_at',
            'modified_at',
        )


class ContentRelatedField(serializers.Field):

    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        if isinstance(value.content_object, Audio):
            serializer = AudioSerializer(value.content_object)
        elif isinstance(value.content_object, Video):
            serializer = VideoSerializer(value.content_object)
        elif isinstance(value.content_object, Text):
            serializer = TextSerializer(value.content_object)
        else:
            raise Exception('Unexpected type of object')

        data = serializer.data
        data['type'] = value.content_type.name
        return data


class ManyContentRelatedField(serializers.ManyRelatedField):
    def to_representation(self, value):
        data = super().to_representation(value)

        content = {}
        for x in data:
            content.setdefault(x['type'], set()).add(x['id'])

        increase_content_counter(content)

        return data


class PageDetailSerializer(PagesSerializer):
    content = ManyContentRelatedField(ContentRelatedField(), read_only=True)

    class Meta:
        model = Page
        fields = (
            'id',
            'url',
            'title',
            'created_at',
            'modified_at',
            'content',
        )
