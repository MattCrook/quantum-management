from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from quantummanagementapp.models import Image


# From for Register view
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


# Form for Login view
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


# Form for the image Form View
class ImageForm(forms.FileInput):
    class Meta:
        model = Image
        fields = ('image', )
