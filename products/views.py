# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Comment, Review, CustomUser
from .forms import ProductForm, CommentForm, ReviewForm, CustomUserChangeForm, SignUpForm
from django.views import View
from django.contrib.auth import login
from django.contrib import messages

class SignUpView(View):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')

        return render(request, self.template_name, {'form': form})
    
# List of products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Product detail view
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product)
    reviews = Review.objects.filter(product=product)
    return render(request, 'products/product_detail.html', {'product': product, 'comments': comments, 'reviews': reviews})

# Create a new product
@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Make sure request.user is a CustomUser instance
            product.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm()

    return render(request, 'products/create_product.html', {'form': form})

# User profile view
@login_required
def user_profile(request, username=None):
    # If the username is not provided, use the currently logged-in user's username
    if username is None:
        username = request.user.username

    user = get_object_or_404(CustomUser, username=username)
    products = Product.objects.filter(seller=user)
    return render(request, 'registration/user_profile.html', {'user': user, 'products': products})

# Edit profile view
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('user_profile', username=request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})

# Add a new comment to a product
@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = CommentForm()

    return render(request, 'products/add_comment.html', {'form': form, 'product': product})

# Add a new review to a product
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ReviewForm()

    return render(request, 'products/add_review.html', {'form': form, 'product': product})

# Search for products
def product_search(request):
    query = request.GET.get('q')
    results = Product.objects.filter(title__icontains=query)
    return render(request, 'products/search_results.html', {'results': results, 'query': query})
