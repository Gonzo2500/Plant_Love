from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from memberships.models import Membership
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Creates a user profile model containing user's
    delivery details, order history and membership type
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE,
                                   default="", blank=True)
    user_phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                      message="Enter phone number in a format:"
                                      "'+111111111' and no longer that "
                                      "15 digits.")
    user_phone_number = models.CharField(validators=[user_phone_regex],
                                         max_length=16, default="",
                                         blank=True)
    user_address_line_1 = models.CharField(max_length=100, default="",
                                           blank=True)
    user_address_line_2 = models.CharField(max_length=100, default="",
                                           blank=True)
    user_city = models.CharField('city or town', max_length=85, default="",
                                 blank=True)
    user_region = models.CharField('region or county', max_length=85,
                                   default="", blank=True)
    user_country = CountryField(blank_label='Country',
                                default="", blank=True)
    user_postcode = models.CharField('post/zip code', max_length=10,
                                     default="", blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    If user doesn't have a profile, create one,
    otherwise save it
    """
    if created:
        Profile.objects.create(user=instance)
    # Save the profile for existing users
    instance.profile.save()
    