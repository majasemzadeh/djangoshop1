from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import BaseManager
from django.contrib.auth.models import UserManager, AbstractUser
# Create your models here.


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    deleted_timestamp = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name=_('Deleted Datetime'),
        help_text=_('This is deleted datetime')
    )
    is_delete = models.BooleanField(
        default=False,
        verbose_name=_('Deleted status'),
        help_text=_('This is deleted status')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Activate status'),
        help_text=_('This is activate status')
    )
    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.is_delete = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()


class MyUserManager(UserManager):
    def _create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super()._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        # username= extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class Myuser(AbstractUser):
    objects = MyUserManager()
    phone = models.CharField(max_length=13, unique=True)
    USERNAME_FIELD = 'phone'