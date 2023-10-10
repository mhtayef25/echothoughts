from django.conf import settings
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='profile/photo')

class Category(models.Model):
    title = models.CharField(max_length=32)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='blogs')
    header = models.TextField()
    cover_photo = models.ImageField(upload_to='blog/cover_photo/')
    STATUS_UNDECIDED = 'u'
    STATUS_PUBLISHED = 'p'
    STATUS_SECRET = 's'
    STATUS_CHOICES = [
        (STATUS_UNDECIDED,'Undecided'),
        (STATUS_PUBLISHED,'Published'),
        (STATUS_SECRET,'Secret'),
    ]
    status = models.CharField(choices=STATUS_CHOICES,default=STATUS_UNDECIDED,max_length=1)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

class Section(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='sections')
    header = models.TextField()
    content = models.TextField(blank=True,null=True)
    photo = models.ImageField(upload_to='blog/section_photo/')

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='commenters')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)