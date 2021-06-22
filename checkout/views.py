from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from shopping_cart.contexts import cart_contents
from .forms import OrderForm
from profiles.forms import ProfileForm
from products.models import Product
from profiles.models import Profile
from .models import OrderLine, Order, DeliveryType

import stripe
import json


@require_POST
def cache_checkout(request):
    """
    Captures data from stripe and saves it
    in stripe PaymentIntent
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_details': request.POST.get('save_details'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Nope.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    A view that renders the checkout and saves the data user has
    put into the order info form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Get data out of the submitted form
        cart = request.session.get('cart', {})

        # Get Delivery Type Instance
        # delivery_type_value = request.POST['delivery_type']
        delivery_type_value = request.session['delivery']
        delivery_type = DeliveryType.objects.get(name=delivery_type_value)

        order_info = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'city': request.POST['city'],
            'region': request.POST['region'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'delivery_type': delivery_type
        }
        # Save the data in Order Form if valid
        order_form = OrderForm(order_info)
        if order_form.is_valid():
            # prevent repetition in saving form
            order = order_form.save(commit=False)

            # get pid from HTML hidden input
            pid = request.POST.get('client_secret').split('_secret')[0]

            # Set stripe_pid and original_cart values for the order instance
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for product_id, qty in cart.items():
                # Loop through items in the cart and add an instance of each
                # to the OrderLine model
                try:
                    product = Product.objects.get(id=product_id)
                    order_line = OrderLine(
                        order=order,
                        product=product,
                        quantity=qty,
                    )
                    order_line.save()
                except Product.DoesNotExist:
                    # Display an error message if something goes wrong
                    messages.error(request, (
                        "There was an issue with an item in your cart. "
                        "Try again later or contact us for assistance!")
                    )
                    # Delete the order and redirect back to the cart
                    order.delete()
                    return redirect(reverse('cart'))

            # Add save-details value to session
            request.session['save_details'] = 'save-details' in request.POST
            # Navigate user to the success checkout page
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            # If form is not valid, display an error message
            messages.error(request, 'There was an error with your form. '
                                    'Please double check your information.'
                                    'Did you enter a valid phone number?')
            return redirect(reverse('checkout'))
    else:
        # If request not POST, get cart contents. if empty, return an error msg
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your cart is empty :(')
            return redirect(reverse('products'))

        # Get total of the cart as an integer
        cart_now = cart_contents(request)
        total = cart_now['grand_total']
        stripe_total = round(total * 100)
        # Set the api key and create stripe intent with amount and currency
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # If user is logged in, try to preefill the checkout form with
        # their saved details, leave blank otherwise.
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.user.first_name,
                    'last_name': profile.user.last_name,
                    'email': profile.user.email,
                    'phone_number': profile.user_phone_number,
                    'address_line_1': profile.user_address_line_1,
                    'address_line_2': profile.user_address_line_2,
                    'city': profile.user_city,
                    'region': profile.user_region,
                    'country': profile.user_country,
                    'postcode': profile.user_postcode,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    delivery_type = request.session['delivery']
    delivery = get_object_or_404(DeliveryType, name=delivery_type)
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'delivery_selected': True,
        'delivery': delivery,
    }

    return render(request, template, context)


def delivery(request):
    """
    Update delivery type and pass it on to checkout
    """
    if request.method == 'POST':
        delivery_num = request.POST.get('delivery_type')
        delivery = get_object_or_404(DeliveryType, pk=delivery_num).name
        request.session['delivery'] = delivery

        return redirect(reverse('checkout'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Render successful order view with the order summary
    displayed and a message that thge order was successfully
    proccessed.
    """
    # Display a success message
    order = get_object_or_404(Order, order_number=order_number)
    save_details = request.session.get('save_details')

    if request.user.is_authenticated:
        #  If user has logged in, attach their profile to the order
        profile = Profile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        # If the user has ticked 'save_details', save them in the profile
        if save_details:
            user_details = {
                'user_phone_number': order.phone_number,
                'user_address_line_1': order.address_line_1,
                'user_address_line_2': order.address_line_2,
                'user_city': order.city,
                'user_region': order.region,
                'user_country': order.country,
                'user_postcode': order.postcode,
            }
            profile_form = ProfileForm(user_details, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    # Calculate discount applied if any
    discount = round((order.subtotal - (order.total - order.delivery_cost)) /
                     order.subtotal * 100, 0)

    # delete cart contents
    if 'cart' in request.session:
        del request.session['cart']

    if 'delivery' in request.session:
        del request.session['delivery']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'discount': discount,
    }

    return render(request, template, context)
