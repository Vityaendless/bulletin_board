from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class AppUser(AbstractUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False, verbose_name="Email")
    avatar = models.ImageField(upload_to='user_pics', verbose_name='Avatar')
    phone = models.CharField(max_length=16, validators=[MinLengthValidator(16)], null=False, blank=False, verbose_name="Phone number")
    ads_count = models.IntegerField(default=0, verbose_name='Ads count')
    comments_count = models.IntegerField(default=0, verbose_name='Comments count')

    def __str__(self):
        return f'{self.first_name} {self.last_name}, username: {self.username}'
