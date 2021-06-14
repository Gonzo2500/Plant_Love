# Create your models here.
import math
import uuid
#  import ColorField for Color.color_hex
from colorfield.fields import ColorField
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Category(models.Model):
    """
    Creates a category model containing the names of
    product categories
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)

    # Change string representation of the object
    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Creates Product model containing data about each individual
    product
    """
    # Allows user to indicate if product will come in multiple colors
    YES = 'Y'
    NO = 'N'
    MANY_COLORS = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    product_code = models.CharField(max_length=36, default=uuid.uuid4,
                                    editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    avg_rating = models.DecimalField('average product rating', max_digits=2,
                                     decimal_places=1, default=0,
                                     null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    many_colors = models.CharField(max_length=1,
                                   choices=MANY_COLORS,
                                   help_text=('Will the product come in '
                                              'multiple colors?'))
    main_pic = models.ImageField('thumbnail picture', null=True, blank=True)
    pic2 = models.ImageField('additional picture 2', null=True, blank=True)
    pic3 = models.ImageField('additional picture 3', null=True, blank=True)
    pic4 = models.ImageField('additional picture 4', null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField('product release date',
                                        help_text=('Select today/now as the '
                                                   'input if the product is '
                                                   'being published now.'))

    def clean(self):
        """
        Raise a validation error if release date is set in past,
        price is set to 0 and below or both
        """
        print(self.price)
        if not self.price:
            raise ValidationError()
        if self.price <= 0 and self.release_date.day < timezone.now().day:
            raise ValidationError(_("Price has to be a positive number and "
                                    "Release Date can't be in past."))
        elif self.price <= 0:
            raise ValidationError(_("Price has to be a positive number."))
        elif self.release_date.day < timezone.now().day:
            raise ValidationError(_("Release date can't be in past."))

    def release_countdown(self):
        """
        Return time to release in days or hours of there are
        less than 1 days left
        """
        date_now = timezone.now()
        if self.release_date > date_now:
            countdown = self.release_date - date_now
            countdown_days = countdown.days
            # Calculate hours using .seconds
            countdown_hours = math.ceil(countdown.seconds / (60*60))
            if countdown_days < 1:
                countdown_display = f'{countdown_hours} hours'
                return countdown_display

            countdown_display = f'{countdown_days} days'
            return countdown_display

    def __str__(self):
        return self.name


class Color(models.Model):
    """
    Creates a Color model containing all colors added to
    each product. These are used if a product comes in more
    than one color
    """
    name = models.CharField(max_length=20)
    color_hex = ColorField(default='#FFFFFF')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return self.name