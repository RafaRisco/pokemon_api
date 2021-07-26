from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q
from decimal import Decimal

# from django.db.models.signals import pre_save
from django.utils import timezone
from django.conf import settings

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
        if not email:
            raise ValueError("Necesitas un email para crear una cuenta")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, is_staff, is_superuser, **kwargs):
        return self._create_user(email, password, False, False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        user = self._create_user(email, password, True, True, **kwargs)
        user.save(using=self._db)
        return user

# the normal user model that allows to adapt the fields
class User(AbstractBaseUser, PermissionsMixin):
    email                                   = models.EmailField(max_length=254, unique=True)
    name                                    = models.CharField(max_length=100)
    surname                                 = models.CharField(max_length=100)
    is_staff                                = models.BooleanField(default=False)
    is_superuser                            = models.BooleanField(default=False)
    is_active                               = models.BooleanField(default=True)
    last_login                              = models.DateTimeField(null=True, blank=True)
    date_joined                             = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
