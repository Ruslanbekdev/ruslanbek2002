from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
# Create your models here.

class ArticleMenager(models.Manager):
    def search(self, query):
        lookups = Q(title__icontains = query) | Q(content__icontains = query)
        obj = Articles.objects.filter(lookups)
        return obj
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tag}'
class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True,  blank=True, unique=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to = 'articles', null = True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    objects = ArticleMenager()

    def __str__(self):
        return f'{self.title} - {self.id} - {self.content}'
    # def get_absolute_url(self):
    #     return f'{self.created_at.year}/{self.created_at.month}/{self.created_at.day}/{self.slug}'
    def get_absolute_url(self):
        return reverse('detail_index', kwargs={'slug':self.slug})
    
    
    # def save(self, *args, **kwargs):
    #     if slugify is None:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
@receiver(pre_save, sender = Articles)
def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)
        print("Pre sav eworking")
        print(args, kwargs)
#-----pre_save.connect(article_pre_save, sender  = Articles)

@receiver(post_save, sender = Articles)
def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()
        print("post save working")
        print(args, kwargs)
#post_save.connect(article_post_save, sender = Articles)
