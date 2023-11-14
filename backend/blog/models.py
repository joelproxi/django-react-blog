from django.db import models

from accounts.models import UserModel


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('-name',)


class Post(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    POST_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/post/')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='categories')
    status = models.CharField(
        max_length=1,
        choices=POST_STATUS,
        default=DRAFT
    )
    author = models.ForeignKey(
       UserModel,
       on_delete=models.CASCADE,
       related_name='posted'
    )
    cretead = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)


class comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='posts')
    author = models.ForeignKey(UserModel,
                               on_delete=models.CASCADE,
                               related_name='commented')
    content = models.TextField()
    cretead = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
