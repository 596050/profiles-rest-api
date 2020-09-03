from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, profile_image=None, phone=None, event_description=None, event_date=None, event_guest_count=None, event_type=None, event_postcode=None, event_address=None, event_cancelled=None, event_budget=None, event_dietary=None, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, profile_image=profile_image, phone=phone, event_description=event_description, event_date=event_date, event_guest_count=event_guest_count,
                          event_type=event_type, event_postcode=event_postcode, event_address=event_address, event_cancelled=event_cancelled, event_budget=event_budget, event_dietary=event_dietary)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_image = models.CharField(max_length=300, null=True, default=None)
    phone = models.CharField(max_length=20, null=True, default=None)
    event_description = models.CharField(
        max_length=1000, null=True, default=None)
    event_date = models.DateField(null=True, default=None)
    event_guest_count = models.IntegerField(null=True, default=None)
    event_type = models.CharField(max_length=50, null=True, default=None)
    event_postcode = models.CharField(max_length=20, null=True, default=None)
    event_address = models.CharField(max_length=20, null=True, default=None)
    event_cancelled = models.BooleanField(default=False, null=True)
    event_budget = models.IntegerField(null=True, default=None)
    event_dietary = models.CharField(max_length=50, null=True, default=None)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
