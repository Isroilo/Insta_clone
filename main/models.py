from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class User(AbstractUser):
    bio = models.TextField(blank=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        unique=True,
        db_index=True,
        validators=[
            RegexValidator(
                regex='^\+998\d{9}$',
                message="Invalid phone number",
                code = "Invalid_number"
            )
        ]
    )
    avatar = models.ManyToManyField('Image', blank=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = ("UserProfile")
        verbose_name_plural = ("UserProfiles")


class Image(models.Model):
    image = models.ImageField(upload_to='user_images/')


class Post(models.Model):
    title = models.CharField(max_length=255)











