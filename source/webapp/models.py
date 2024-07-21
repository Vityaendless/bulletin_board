from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


STATUSES = [('1', 'Moderate'), ('2', 'Approve'), ('3', 'Rejection'), ('4', 'On delete')]
USER = get_user_model()


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True


class Ad(AbstractModel):
    photo = models.ImageField(upload_to='publications_images', null=True, blank=True, verbose_name='Photo')
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Title")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Description")
    author = models.ForeignKey(USER, null=False, blank=False, related_name='ads', on_delete=models.CASCADE, verbose_name="Author")
    category = models.ForeignKey('webapp.Category', related_name='ads', on_delete=models.CASCADE, verbose_name='Category')
    price = models.FloatField(default=0, verbose_name='Price')
    status = models.CharField(max_length=30, null=False, blank=False, verbose_name='Category', choices=STATUSES, default=1)
    published_at = models.DateTimeField(verbose_name="Published at", null=True, blank=True)

    def __str__(self):
        return f"This is ad {self.id}, {self.title}"

    def get_absolute_url(self):
        return reverse('webapp:ad_view', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=20,blank=False, null=False, verbose_name='Category name')

    def __str__(self):
        return self.name


class Comment(AbstractModel):
    text = models.TextField(max_length=500, null=False, blank=False, verbose_name='Comment')
    author = models.ForeignKey(USER, related_name='comments', null=False, blank=False, on_delete=models.CASCADE, verbose_name="Author")
    ad = models.ForeignKey('webapp.Ad', related_name='comments', on_delete=models.CASCADE, verbose_name='Ad')

    def __str__(self):
        return self.text[:20]
