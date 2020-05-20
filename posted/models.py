from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Elements(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

class Post(models.Model):
    category = models.ManyToManyField(Category, blank=False)
    tags = models.ManyToManyField(Tag, blank=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='post_images/', null=True, blank=True)
    like = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('post_update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('delete_update', kwargs={
            'id': self.id
        })
    
    @property
    def get_comments(self):
        return self.comments.all()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

# Goodクラス
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_owner')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'good for "' + str(self.post) + '" (by ' + str(self.owner) + ')'

# class Original(models.Model):
#     category = models.ManyToManyField(Category, blank=True)
#     tags = models.ManyToManyField(Tag, blank=True)
#     elements = models.ManyToManyField(Elements, blank=True)
#     add_element = models.CharField(blank=True, max_length=200)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     is_public = models.BooleanField(default=True)
#     published_at = models.DateTimeField(blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if self.is_public and not self.published_at:
#             self.published_at = timezone.now()
#         super().save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username