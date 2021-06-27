import uuid

from decimal import Decimal


from django.db import models
from django.db.models import Sum
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import Profile


class DeliveryType(models.Model):
    """
    Creates Delivery Type Model containing specific
    data on each specific delivery type
    """
    name = models.CharField('Delivery Type', max_length=20)
    dispatch_speed = models.IntegerField('days to dispatch order')
    delivery_speed = models.IntegerField('days to deliver order')
    limit = models.DecimalField('order amount limit for set delivery cost',
                                max_digits=5, decimal_places=2, default=0)
    const = models.DecimalField('set delivey cost', max_digits=5,
                                decimal_places=2, default=0)
    rate = models.DecimalField('delivery rate', max_digits=5,
                               decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Creates Order Model containing data on each order
    which also potentially contains multiple products
    """
    order_number = models.CharField(max_length=36, default=uuid.uuid4,
                                    editable=False)
    user_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                     default="", blank=True,
                                     related_name='user_orders')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=70, editable=False,
                                 default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Enter phone number in a format: "
                                         "'+111111111' and no longer that "
                                         "15 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16,
                                    default=0)
    email = models.EmailField(max_length=254)
    address_line_1 = models.CharField(max_length=100,)
    address_line_2 = models.CharField(max_length=100, default="", blank=True)
    city = models.CharField('city or town', max_length=85)
    region = models.CharField('region or county', max_length=85, default="",
                              blank=True)
    country = CountryField(blank_label='Country *')
    postcode = models.CharField('post/zip code', max_length=10)
    order_date = models.DateTimeField(auto_now_add=True)
    dispatch_date = models.DateTimeField('order dispatched on',
                                         default="", blank=True)
    est_dispatch_dte = models.DateTimeField('estimated order dispatch date',
                                            editable=False, default="",
                                            blank=True)
    delivery_date = models.DateTimeField('order delivered on',
                                         default="", blank=True)
    est_deliery_dte = models.DateTimeField('estimated order delivery date',
                                           editable=False, default="",
                                           blank=True)
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE)
    delivery_cost = models.DecimalField(max_digits=7, decimal_places=2,
                                        default=0)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    original_cart = models.TextField(default='')
    stripe_pid = models.CharField(max_length=254, default='')

    def total_amount(self):
        """
        Calculate the subtotal, delivery cost and the total,
        depending on the delivery type selected and products
        in the order
        """
        self.subtotal = self.order_line.aggregate(
            Sum('line_total'))['line_total__sum'] or 0
        if self.subtotal < self.delivery_type.limit:
            self.delivery_cost = self.delivery_type.const
        else:
            self.delivery_cost = self.subtotal * Decimal(
                self.delivery_type.rate / 100)
        self.total = self.subtotal + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Calculate fields when Order is saved based
        on membership and delivery type
        """
        # Get delivery and dispatch dates
        date_now = timezone.now()
        dispatch_days = timezone.timedelta(
            days=self.delivery_type.dispatch_speed)
        delivery_days = timezone.timedelta(
            days=self.delivery_type.delivery_speed)
        self.est_dispatch_dte = date_now + dispatch_days
        self.est_deliery_dte = date_now + delivery_days
        # Order number in uppercase
        self.order_number = str(self.order_number).upper()
        # Full name
        self.full_name = f'{self.first_name} {self.last_name}'

        # If logged in user, calculate delivery amount and discount
        if self.user_profile and self.user_profile.membership:
            # Get order count for the user
            user_orders_count = Order.objects.filter(
                user_profile=self.user_profile).count()
            # If paid memebrship, apply free delivery
            if self.user_profile.membership.name != 'Basic':
                self.delivery_cost = 0
                # Discount for the first order
                if user_orders_count == 0:
                    discount = self.user_profile.membership.first_order_disc
                # Discount for all other orders
                else:
                    discount = self.user_profile.membership.overall_discount
            # Unpaid memebrship
            else:
                # Discount for the first order
                if user_orders_count == 0:
                    discount = self.user_profile.membership.first_order_disc
                # No overall discount
                else:
                    discount = 0

            # Calculate total with delivery and discount
            discount_price = round(self.subtotal * Decimal(discount / 100), 2)
            self.total = self.subtotal + self.delivery_cost - discount_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLine(models.Model):
    """
    Creates OrderLine Model containing data on each product
    added to the cart
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='order_line')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, default="", blank=True)
    quantity = models.IntegerField(default=0)
    line_total = models.DecimalField(max_digits=7, decimal_places=2,
                                     default=0, editable=False)

    def save(self, *args, **kwargs):
        """
        Calculate the total of a line item before saving
        an entry
        """
        self.line_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def clean(self):
        """
        Raise an Error if quantity entered is <1 or >10
        """
        if self.quantity < 1 or self.quantity > 10:
            raise ValidationError(_('Please enter valid quantity.'
                                    'Max 10 of the same product per person'))

    def __str__(self):
        """
        String Represention of the object
        """
        return f'{self.product.name} in order {self.order.order_number}'
        