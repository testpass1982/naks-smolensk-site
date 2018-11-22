from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# from django_resized import ResizedImageField


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=64)
    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)
    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

class ContentMixin(models.Model):
    #base class for Post, Article and Documents
    title = models.CharField(u'Название', max_length= 200)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    published_date = models.DateTimeField(u'Дата публикации', blank=True, null=True)
    created_date = models.DateTimeField(u'Дата создания', default=timezone.now)
    text = RichTextUploadingField(verbose_name='Текст')
    author = models.ForeignKey('auth.User', verbose_name='Автор', on_delete=models.CASCADE)
    publish_on_main_page = models.BooleanField(verbose_name="Опубликовать на главной", default=False)

    class Meta:
        abstract = True

class Post(ContentMixin):
    #child of ContentMixin
    category = models.ForeignKey(Category, verbose_name='Категория',on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created_date']
        get_latest_by = ['created_date']
        verbose_name = 'Страница'
        verbose_name_plural = "Страницы"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(ContentMixin):
    #child of ContentMixin

    short_description = models.CharField(u'Краткое описание', max_length=200, blank=True)

    class Meta:
        ordering = ['created_date']
        get_latest_by = ['created_date']
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(u'Название', max_length=500)
    document = models.FileField(verbose_name='Документ', upload_to="documents/", 
        validators = [FileExtensionValidator(allowed_extensions = ['pdf', 'docx', 'doc', 'jpg', 'jpeg'], message="Неправильный тип файла, используйте PDF, DOCX, DOC, JPG, JPEG")])
    uploaded_at = models.DateTimeField(verbose_name='Загружен', default=timezone.now)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    post = models.ForeignKey(Post, verbose_name='Страница', blank=True, default='', on_delete=models.SET_NULL, null=True)
    publish_on_main_page = models.BooleanField(verbose_name="Опубиковать на главной", default=False)
    
    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return "upload/{post_pk}/{filename}{extension}".format(
        post_pk=instance.pk,
        filename=slugify(filename_base),
        extension=filename_ext.lower(),)

def get_image_filename():
    return f'image_{slugify(timezone.now())}'

class PostPhoto(models.Model):
    post = models.ForeignKey(Post, verbose_name=u'новость', related_name='images', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(u'изображение', upload_to="upload/")
    title = models.CharField(u'название', max_length=64, blank=True, default=get_image_filename)
    position = models.PositiveIntegerField(u'Позиция', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
        ordering = ['position']
    def __str__(self):
        return f'{self.post} - {self.image}'

class Message(models.Model):
    title = models.CharField(u'Заголовок', max_length=64, blank=True)
    typeof = models.CharField(u'Тип сообщения', max_length=64, blank=True)
    params = models.CharField(u'Параметры сообщения', max_length=512, blank=True)
    sender_email = models.EmailField(u'Адрес электронной почты', max_length=64, blank=True)
    sender_phone = models.CharField(u'Телефон', max_length=64, blank=True)
    created_date = models.DateTimeField(u'Дата получения', default=timezone.now)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title

        


    

    