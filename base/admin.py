from django.contrib import admin

from base.models import Page, Audio, Video, Text, PageContent


class PageContentInline(admin.TabularInline):
    model = PageContent
    extra = 1


class PageAdmin(admin.ModelAdmin):
    # https://code.djangoproject.com/ticket/6933
    search_fields = (
        '^title',
    )
    inlines = (PageContentInline,)


class AudioAdmin(admin.ModelAdmin):
    pass


class TextAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Video, VideoAdmin)
