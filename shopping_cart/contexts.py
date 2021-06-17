from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product
from checkout.models import DeliveryType
from profiles.models import Profile
from memberships.models import Membership
from checkout.models import Order


def cart_contents(request):
    """
    Define a context dictionary cart_contents
    to be used accross all apps
    """
    cart_items = []
    subtotal = 0
    item_count = 0
    delivery_type = None
    delivery_cost = 0
    discount = 0

    # retrieve cart session dictionary or initialize
    cart = request.session.get('cart', {})

    # Loop thorugh items in the cart
    for product_id, qty in cart.items():
        # Retrieve the product and get the quantity
        product = get_object_or_404(Product, pk=product_id)
        product_total = qty * product.price
        item_count += qty
        # Calculate total price of each type of items
        subtotal += qty * product.price
        # Add these values to cart_items to be used globally
        cart_items.append({
            'product_id': product_id,
            'quantity': qty,
            'product': product,
            'product_total': product_total,
        })

    delivery_type = request.session.get('delivery', '')

    # If there is a session variable with delivery type
    # meaning that a person is checkin out
    if delivery_type:
        delivery = DeliveryType.objects.get(name=delivery_type)
        # Check membership type for logged in user and
        if request.user.is_authenticated:
            user = get_object_or_404(Profile, user=request.user)
            # If user has paid memebrship, set delivery cost to 0
            if user.membership and user.membership.name != 'Basic':
                delivery_cost = 0
            # Otherwise calculate delivery cost
            else:
                if subtotal < delivery.limit:
                    delivery_cost = delivery.const
                else:
                    delivery_cost = round(
                        subtotal * Decimal(delivery.rate / 100), 2)
        # If user has not logged in, calculate tehir delivery costs
        else:
            if subtotal < delivery.limit:
                delivery_cost = delivery.const
            else:
                delivery_cost = round(
                    subtotal * Decimal(delivery.rate / 100), 2)
    # If session var does not exist, xset delivery cost to 0
    else:
        delivery_cost = 0

    # Get discount amount based on memebrship and if
    # this is users first order
    if request.user.is_authenticated:
        user = get_object_or_404(Profile, user=request.user)
        if user.membership:
            membership = Membership.objects.get(name=user.membership.name)
            user_orders_count = Order.objects.filter(user_profile=user).count()
            if user_orders_count == 0:
                discount = membership.first_order_disc
            else:
                discount = membership.overall_discount
    # If user is eligble for a discount, calculate it here
    discount_price = round(subtotal * Decimal(discount / 100), 2)
    total = subtotal - discount_price
    grand_total = round((total + delivery_cost), 2)

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total,
        'item_count': item_count,
        'delivery_type': delivery_type,
        'delivery_cost': delivery_cost,
        'grand_total': grand_total,
        'discount': discount,
    }

    return context
    