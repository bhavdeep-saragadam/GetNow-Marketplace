from django import forms
from .models import Product, Comment, Review, CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2', 'bio', 'contact')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'contact', 'bio')
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
        
# forms.py
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']

