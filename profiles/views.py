from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.contrib import messages
from memberships.models import Membership
from .models import Profile
from .forms import ProfileForm
from checkout.models import Order, OrderLine


@login_required
def profile(request):
    """ A view to return the profile page """
    profile = Profile.objects.get(user=request.user)

    if not profile.membership:
        messages.error(request, "You haven't subscribed to a membership yet. "
                                " Choose one and join the Prickly fam")
        return redirect(reverse('memberships'))

    membership = get_object_or_404(Membership, name=profile.membership)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Well done you! Your '
                                      'details were updated :)')
        else:
            messages.error(request, 'Uh oh, something went wrong. '
                                    'Try again and make sure all '
                                    'fields are valid!')
    else:
        profile_form = ProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'membership': membership,
        'profile_form': profile_form,
        'on_profile': True,
    }

    return render(request, template, context)


@login_required
def order_history(request):
    profile = get_object_or_404(Profile, user=request.user)
    orders = Order.objects.filter(user_profile=profile).order_by('-order_date')
    order_items = OrderLine.objects.all()
    last_order_id = orders.aggregate(Max('pk'))

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
        'last_order_id': last_order_id,
        'order_items': order_items,
    }
    return render(request, template, context)


@login_required
def order_details(request, order_id):
    """
    Retrieves specific order details
    """
    # Get the order
    order = get_object_or_404(Order, pk=order_id)
    # Calculate the discount
    discount = round((order.subtotal - (order.total - order.delivery_cost)) /
                     order.subtotal * 100, 0)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'discount': discount,
        'order_details': True,
    }

    return render(request, template, context)
