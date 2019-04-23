from django.contrib import admin

from base.models import Page, Audio, Video, Text, PageContent


class PageContentAdmin(admin.ModelAdmin):
    model = PageContent
    list_display = (
        'id',
        'page',
        'content_type',
        'content_object',
        'order',
    )


class PageContentInline(admin.TabularInline):
    model = PageContent
    extra = 1


class PageAdmin(admin.ModelAdmin):
    # https://code.djangoproject.com/ticket/6933
    search_fields = (
        '^title',
    )
    inlines = (PageContentInline,)

    list_display = (
        'id',
        'title',
        'created_at',
        'modified_at',
    )


class AudioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'counter',
        'audio',
        'bitrate',
        'created_at',
        'modified_at',
    )


class TextAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'counter',
        'get_text_display',
        'created_at',
        'modified_at',
    )

    @staticmethod
    def get_text_display(obj):
        text = obj.text
        if len(text) > 100:
            text = f"{text[:100]}..."
        return text


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'counter',
        'video',
        'subtitles',
        'created_at',
        'modified_at',
    )


admin.site.register(Page, PageAdmin)
admin.site.register(PageContent, PageContentAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Video, VideoAdmin)
