import stripe

from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse

from .models import Membership, StripeCustomer
from profiles.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User


def memberships(request):
    """
    A view to return the memberships page
    """

    # Get all membership model entries
    memberships = Membership.objects.all()
    template = 'memberships/memberships.html'
    if request.user.is_anonymous:
        context = {
            'memberships': memberships,
        }
    else:
        profile = Profile.objects.get(user=request.user)
        if profile.membership:
            user_membership = profile.membership.name
            context = {
                'user_membership': user_membership,
                'memberships': memberships,
            }
        else:
            context = {
                'memberships': memberships,
            }

    return render(request, template, context)


def membership_type(request):
    """
    Capture membership type selected by user, store it in
    session variable and redirect user to the signup page
    """

    membership_type = request.POST.get('membership_type')
    request.session['membership'] = membership_type
    if request.user.is_authenticated:
        return redirect(reverse('membership_checkout'))

    return redirect(reverse('account_signup'))


@login_required
def membership_checkout(request):
    """
    Retrieve user selected membership, display it and
    benefits, and allow user to change the membership
    type
    """
    # Retrieve data for all memberships
    all_memberships = Membership.objects.all()

    # Check if user already has a memership and got to this
    # page by accident, then re-direct to change site
    profile = Profile.objects.get(user=request.user)
    if profile.membership:
        return redirect(reverse('membership_change'))
    # If user is updating selected membership, the
    # memberhip_type to the new value
    if request.GET.get('membership-new'):
        membership_type = request.GET.get('membership-new')
        # add membership type to session to retrieve for stripe
        request.session['membership'] = membership_type
    # If user logged in after
    # registering, get membership_type from session
    else:
        try:
            # Retrieve user selected membership
            membership_type = request.session['membership']
        except KeyError:
            # If user logged in normally, redirect them
            # to the profile page
            return redirect(reverse('products'))

    # Retrieve data for selected membership type
    membership = get_object_or_404(Membership, name=membership_type)

    template = 'memberships/membership_checkout.html'
    context = {
        'membership': membership,
        'all_memberships': all_memberships,
    }

    return render(request, template, context)


@login_required
def user_membership_view(request):
    """
    Displays user's membership view with details
    """
    profile = Profile.objects.get(user=request.user)

    if not profile.membership:
        messages.error(request, "You haven't subscribed to a membership yet. "
                                " Choose one and join the Prickly fam")
        return redirect(reverse('memberships'))

    membership = get_object_or_404(Membership, name=profile.membership)
    context = {
        'membership': membership,
    }
    template = 'memberships/user_membership.html'

    return render(request, template, context)


@login_required
def membership_change(request):
    """
    Handles membership change and adding selected memebrship
    to the session
    """
    profile = Profile.objects.get(user=request.user)
    if not profile.membership:
        return redirect(reverse('memberships'))

    if not request.POST.get('membership_type'):
        return redirect(reverse('memberships'))

    all_memberships = Membership.objects.all()
    membership_type = request.POST.get('membership_type')
    request.session['membership'] = membership_type
    membership = get_object_or_404(Membership, name=membership_type)
    template = 'memberships/membership_checkout.html'

    context = {
        'change_membership': True,
        'membership': membership,
        'all_memberships': all_memberships,
    }
    return render(request, template, context)


@login_required
def membership_update(request):
    """
    Update user's membership in the stripe system
    and our database too
    """

    if not Profile.objects.get(user=request.user).membership:
        return redirect(reverse('memberships'))

    stripe.api_key = settings.STRIPE_SECRET_KEY
    # user's chosen membership
    membership = request.session['membership']

    # Asign correct price keys to the paid memberships
    if membership == 'Ultimate':
        price = settings.STRIPE_PRICE_ID_ULTIMATE
    elif membership == 'Supreme':
        price = settings.STRIPE_PRICE_ID_SUPREME
    else:
        price = settings.STRIPE_PRICE_ID_BASIC

    # Check if the user already exists in stripe system and
    # our database
    try:
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        subscription = stripe.Subscription.retrieve(
            stripe_customer.stripeSubscriptionId)
        # Update existing membership with a new one
        stripe.Subscription.modify(
            subscription.id,
            cancel_at_period_end=False,
            proration_behavior='create_prorations',
            items=[{
                'id': subscription['items']['data'][0].id,
                'price': price,
            }]
        )

        # Attach new membership to the user's profile
        membership_type = get_object_or_404(Membership, name=membership)
        profile = get_object_or_404(Profile, user=request.user)
        profile.membership = membership_type
        profile.save()

        messages.success(request, 'Congrats!! You successfully changed'
                                  ' your membership to the '
                                  f'{membership} membership!')
        # Redirect the user to profiles page
        return redirect(reverse('profile'))

    # If user doesn't exist, return error
    except StripeCustomer.DoesNotExist:
        return messages.error(request, 'User does not exist')


"""
The following code was taken from
https://testdriven.io/blog/django-stripe-subscriptions/
and
https://stripe.com/docs/billing/subscriptions/checkout
It is used to set up Stripe external checkout form
to handle subscriptions and was customized
"""


@csrf_exempt
def stripe_config(request):
    """
    Handles AJAX requests coming from stripe_sub.js
    """
    if request.method == 'GET':
        # add public key in a dict that will be retrieved by JS
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    """
    Creates the Checkout Session with product details
    and returns Checkout Session ID to be fetched by
    frontend
    """
    if request.method == 'GET':
        # define domain URL
        domain_url = settings.DOMAIN_URL
        # set stripe API from SECRET KEY variable
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # get user chosen membership from session
        membership = request.session['membership']
        # set stripe product price dependant on above
        if membership == 'Ultimate':
            price = settings.STRIPE_PRICE_ID_ULTIMATE
        elif membership == 'Supreme':
            price = settings.STRIPE_PRICE_ID_SUPREME
        else:
            price = settings.STRIPE_PRICE_ID_BASIC

        # Create session that will be passed to stripe
        # with new membership details
        try:
            # Create a Checkout Session
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=(request.user.id if
                                     request.user.is_authenticated else None),
                # link to checkout success page if paymenr successful
                success_url=(
                    domain_url + 'success?session_id={CHECKOUT_SESSION_ID}'),
                #  Link to a page if user cancels the payment in checkout
                cancel_url=domain_url + 'membership_checkout/',
                # Define payment method to be a card
                payment_method_types=['card'],
                # Subscription model
                mode='subscription',
                # Price and quantity of items
                line_items=[
                    {
                        'price': price,
                        'quantity': 1,
                    }
                ]
            )
            # Return Checkout Session ID
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    """
    Display profile page and the membership details
    when a user has succesfully subscribed
    """
    profile = get_object_or_404(Profile, user=request.user)
    if not profile.membership:
        membership_type_value = request.session['membership']
        membership_type = Membership.objects.get(name=membership_type_value)
        profile.membership = membership_type
        profile.save()

    membership = get_object_or_404(Profile, user=request.user).membership.name

    # Add a success message
    messages.success(request, 'Congrats!! You successfully'
                              ' subscribed to the '
                              f'{membership} membership!')
    # Redirect the user to profiles page
    return redirect(reverse('profile'))


@csrf_exempt
def stripe_webhook(request):
    """
    Create a new StripeCustomer every time someone subscribes
    to the membership by using Stripe Webhook
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET_SUB
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Return status 400 if payload is invalid
        messages.error(request, f'error: {e}')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Return status 400 if signature is invalid
        messages.error(request, f'error: {e}')
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')
        # get total of the product subscribtion
        total = session.get('amount_total')
        total_num = round(total / 100, 2)
        # get membership type based on the price
        membership_type = get_object_or_404(Membership, price=total_num)
        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        # Update user profile with the membership details
        profile = get_object_or_404(Profile, user=user)
        profile.membership = membership_type
        profile.save()

    return HttpResponse(status=200)
