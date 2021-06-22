from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Avg

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import Profile


def add_review(request, product_id):
    """
    Allow user to add a review and redirect them back to the
    item product item view
    """
    # Get current user and product
    user = Profile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    # Initiate review form
    review_form = ReviewForm()
    # Get details submitted by the user
    review_details = {
        'title': request.POST['title'],
        'description': request.POST['description'],
        'rating': request.POST['rating'],
    }
    # Add details to the form
    review_form = ReviewForm(review_details)

    # Check if the user has already reviewed the item
    existing_review = Review.objects.filter(user=user, product=product)
    # If count of reviews is > 0, return an erro
    if existing_review.count() > 0:
        messages.error(request, 'You have already reviewed this item!')

    # If no reviews are found, add the review
    else:
        # If form is valid, add user and product and save
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = user
            review.product = product
            review.save()

            # Update average rating for the product
            reviews = Review.objects.filter(product=product)
            avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.avg_rating = int(avg_rating)
            product.save()

            # Success message if added
            messages.success(request, 'Thanks! Your review was added :)')
        else:
            # Error message if form was invalid
            messages.error(request, 'Uh oh, something went wrong. '
                                    'Make sure the form is valid.')

    return redirect(reverse('product_item', args=(product_id,)))


def edit_review(request, review_id):
    """
    Saves review form edited by user
    """
    # get the review and review form
    review = get_object_or_404(Review, pk=review_id)
    review_form = ReviewForm(request.POST, instance=review)
    product = Product.objects.get(name=review.product)
    # If form is valid, save it
    if review_form.is_valid():
        review.save()

        # Update average rating for the product
        reviews = Review.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        product.avg_rating = int(avg_rating)
        product.save()

        # Success message if added
        messages.success(request, 'Thanks! Your review was edited :)')
    else:
        # Error message if form was invalid
        messages.error(request, 'Uh oh, something went wrong. '
                                'Make sure the form is valid.')

    return redirect(reverse('product_item', args=(review.product.id,)))


def delete_review(request, review_id):
    """
    Deletes user's review
    """
    # get the review and review form
    review = get_object_or_404(Review, pk=review_id)
    product = Product.objects.get(name=review.product)

    # Delete the review and return success message
    try:
        review.delete()

        # Update average rating for the product
        reviews = Review.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        if avg_rating:
            product.avg_rating = int(avg_rating)
        # If all reviews have been deleted
        else:
            product.avg_rating = 0

        product.save()

        messages.success(request, 'Your review was deleted :(')

    # If deletion failed, return an error message
    except Exception as e:
        messages.error(request, "We couldn't delete your review because "
                                f" eroor:{e} occured. Try again later.")

    return redirect(reverse('product_item', args=(review.product.id,)))
