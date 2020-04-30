from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from mda.models import Ministry
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_ministryuser = models.BooleanField(default=False)
    is_governor = models.BooleanField(default=False)
    is_pmp = models.BooleanField(default=False)
    is_budget = models.BooleanField(default=False)
    is_dueprocess = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    ministry = models.ForeignKey(
        Ministry, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def user_type(self):
        if self.is_ministryuser:
            return "Ministry Member"
        elif self.is_governor:
            return "Governor"
        elif self.is_pmp:
            return "PMP"
        elif self.is_budget:
            return "Budget Member"
        elif self.is_dueprocess:
            return "Due Process"
        else:
            return "Administrator"

    def fullname(self):
        return self.first_name + self.last_name

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.user_type


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    print(created)
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
