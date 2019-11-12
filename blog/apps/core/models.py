from django.db import models
# from autoslug import AutoSlugField
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=55, unique=True)

    slug = models.SlugField(default='', blank=True)

    image = models.ImageField(upload_to='post_img',
                              blank=True,
                              null=True)

    desc = models.TextField(max_length=255)

    date_of_publ = models.DateTimeField(auto_now_add=True)

    visible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('core:post_detail', kwargs={'slug': self.slug})

    @property
    def short_desc(self):
        return self.desc[:20] + '...' if len(self.desc) > 20 else self.desc

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    sender_name = models.CharField(max_length=55,blank=True)

    text = models.TextField(max_length=255)

    date_of_publ = models.DateTimeField(auto_now_add=True)
