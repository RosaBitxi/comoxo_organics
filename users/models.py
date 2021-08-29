from datetime import timedelta
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

STATUS = ((0, "Not Approved"), (1, "Approved"))
LOCATIONS = ((0, "Unknown"), (1, "Comoxo"), (2, "Conga"))
STARS = ((1, "Horrible"), (2, "Unsatisfied"),(3, "Neutral"),(4, "Good"),(5, "Excellent"))

TODAY = timezone.now()

def return_date_time_now():
    now = timezone.now()
    return now

def return_date_time_weeks():
    now = timezone.now()
    return now + timedelta(14)

def return_min_age():
    now = timezone.now()
    return now - timedelta(18*365)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=200)
    country = CountryField()
    birthdate = models.DateField(blank=True, default=return_min_age)
    start_date = models.DateField(default=return_date_time_now)
    end_date = models.DateField(default=return_date_time_weeks)
    details = models.TextField(default="blank")
    location = models.IntegerField(choices=LOCATIONS, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
        
    class Meta:
        app_label = 'users'


class Reviews(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="user_review")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = models.IntegerField(choices=STARS, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    location = models.IntegerField(choices=LOCATIONS, default=0)
    pic = models.ImageField(blank=True, null=True, upload_to='reviews', default="https://i.stack.imgur.com/y9DpT.jpg")

    def __str__(self):
        return "Review by {} from {}".format(self.author, self.author.country)
