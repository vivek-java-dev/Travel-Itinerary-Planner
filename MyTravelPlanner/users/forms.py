from typing import Any
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from django import forms
# from .models import ProfileModel

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm,self).__init__(*args, **kwargs)

        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None
            # self.fields[fieldname] = None