from django.db import models

from accounts.models import UserModel


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('-name',)
        indexes = [
            models.Index(
                fields=['slug']
            )
        ]


class CreationModificationMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)
        indexes = [
            models.Index(
                fields=['-created']
            )
        ]


class TimestempContentMixin(CreationModificationMixin):
    content = models.TextField()

    class Meta(CreationModificationMixin.Meta):
        pass


class Post(TimestempContentMixin):
    DRAFT = 'D'
    PUBLISHED = 'P'
    POST_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )
    title = models.CharField(max_length=200)
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

    def __str__(self):
        return self.title


class comment(TimestempContentMixin):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='posts')
    author = models.ForeignKey(UserModel,
                               on_delete=models.CASCADE,
                               related_name='commented')

    def __str__(self):
        return self.content[:30]
