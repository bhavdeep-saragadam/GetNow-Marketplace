from django.urls import path, include
from .views import product_list, create_product, product_detail, add_comment, add_review, SignUpView, product_search,user_profile,edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/create/', create_product, name='create_product'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/<int:product_id>/comment/', add_comment, name='add_comment'),
    path('products/<int:product_id>/review/', add_review, name='add_review'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', SignUpView.as_view(), name='signup'),  # Use your custom SignUpView
    path('search/', product_search, name='product_search'), 
    path('user/profile/', user_profile, name='user_profile'),
    path('user/<str:username>/', user_profile, name='user_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),

    # Include default authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]
