from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from quantummanagementapp.models import Image


# From for Register
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




# Form for the image Form View
class ImageForm(forms.FileInput):
    class Meta:
        model = Image
        fields = ('image', )
