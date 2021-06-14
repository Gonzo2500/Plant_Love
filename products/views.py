from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Color


def all_products(request):
    """
    Return a page with all products displayed,
    Allow user to select category and filter objects by it
    Allow user to sort items
    """
    products = Product.objects.all()
    categories = Category.objects.all()
    item_category = 'All'
    media_url = settings.MEDIA_URL

    # Filter objects by the selected category and save selected category
    if request.GET:
        if 'category' in request.GET:
            item_category = request.GET['category']
            products = products.filter(category__name=item_category)
            # Sorting functionality for all items and each category
            if 'sort' in request.GET:
                sort_by = request.GET['sort']
                if item_category == 'All':
                    products = Product.objects.order_by(sort_by)

                products = products.order_by(sort_by)

    # Search entered keywoard in name, description or category
    if 'search' in request.GET:
        search_query = request.GET['search']
        if not search_query:
            # If user didn't enter a value, return an error message
            messages.error(request, "Please enter a search value.")
            return redirect(reverse('products'))

        # Use icontains to return case insensitive results
        name_q = Q(name__icontains=search_query)
        desc_q = Q(description__icontains=search_query)
        cat_q = Q(category__name__icontains=search_query)
        # Search in either name or description
        combined_query = Q(name_q) | Q(desc_q) | Q(cat_q)
        products = products.filter(combined_query)

    context = {
        'products': products,
        'categories': categories,
        'active_category': item_category,
        'media_url': media_url,
    }

    return render(request, 'products/products.html', context)


def product_item(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    colors = Color.objects.filter(product=product.pk)
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        user = Profile.objects.get(user=request.user)
    else:
        user = None

    # get all reviews for given product
    reviews = Review.objects.filter(product=product)

    # If user has reviewed an item
    try:
        # retrieve review for selected item by user
        item_review = Review.objects.get(user=user, product=product)

        # get a prefilled form with specific review
        edit_review_form = ReviewForm(instance=item_review)

    # If there are no reviews by the user
    except Review.DoesNotExist:
        edit_review_form = None

    review_form = ReviewForm()
    template = 'products/product_item.html'
    context = {
        'product': product,
        'colors': colors,
        'reviews': reviews,
        'review_form': review_form,
        'edit_review_form': edit_review_form,

    }

    return render(request, template, context)
