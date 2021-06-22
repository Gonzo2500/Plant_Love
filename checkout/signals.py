from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLine


@receiver(post_save, sender=OrderLine)
def update_on_save(sender, instance, created, **kwargs):
    """
    Calculates total amount as items are being added to the
    order
    """
    instance.order.total_amount()


@receiver(post_delete, sender=OrderLine)
def update_on_delete(sender, instance, **kwargs):
    """
    Calculate orer total if an item is removed
    """
    instance.order.total_amount()