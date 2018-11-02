from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


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

class Post(models.Model):
    title = models.CharField(max_length= 200)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class File(models.Model):
#     name = models.CharField(max_length=64)
#     file = models.FileField(upload_to="files/")

class Document(models.Model):
    title = models.CharField(max_length=500, blank=True)
    document = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title
    

    