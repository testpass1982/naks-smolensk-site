from django.contrib import admin
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import format_html

from .models import Post, Category, Tag, Document, PostPhoto, Article
# Register your models here.

def get_picture_preview(obj):
    if obj.pk:  # if object has already been saved and has a primary key, show picture preview
        return format_html("""<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
            src=obj.image.url,
            title=obj.title,
        ))
    return "(После загрузки фотографии здесь будет ее миниатюра)"
get_picture_preview.allow_tags = True
get_picture_preview.short_description = "Предварительный просмотр:"

class PostPhotoInline(admin.StackedInline):
    model = PostPhoto
    extra = 0
    fields = ['id', "get_edit_link", "title", "image", "position", get_picture_preview]
    readonly_fields = ['id', "get_edit_link", get_picture_preview]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return format_html("""<a href="{url}">{text}</a>""".format(
                url=url,
                text="Редактировать %s отдельно" % obj._meta.verbose_name,
            ))
        return "(Загрузите фотографию и нажмите \"Сохранить и продолжить редактирование\")"
    get_edit_link.short_description = "Изменить"
    get_edit_link.allow_tags = True

class DocumentInline(admin.StackedInline):
    model = Document
    extra = 0
    fields = ['id', "title", 'document']
    list_display = ['title', 'publish_on_main_page']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_on_main_page']



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # save_on_top = True
    fields = ['id', 'title', 'tags', 'category', 'author', 'text', 'created_date', 'published_date', 'publish_on_main_page']
    readonly_fields = ('id',)
    list_display = ['title', 'category', 'created_date', 'publish_on_main_page']
    inlines = [PostPhotoInline, DocumentInline]

@admin.register(PostPhoto)
class PostPhotoAdmin(admin.ModelAdmin):
    # save_on_top = True
    fields = ['id', "post", "image", "title", "position", get_picture_preview]
    readonly_fields = ['id', get_picture_preview]
    list_display=['title', 'post', get_picture_preview]

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
