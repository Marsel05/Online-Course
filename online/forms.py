from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *

class CustomSignupForm(SignupForm):
    country = forms.CharField(max_length=100, label=_('Country'))
    age = forms.IntegerField(label=_('Age'))
    phone_number = forms.IntegerField(label=_('Phone Number'))
    first_name = forms.CharField(max_length=100, label=_('First Name'))
    last_name = forms.CharField(max_length=100, label=_('Last Name'))
    last_login_date = forms.DateField(label=_('Last Login Date'), widget=forms.DateInput(attrs={'type': 'date'}))
    role = forms.ChoiceField(choices=UserProfile.CHOICES_ROLE, label=_('Role'))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if phone_number < 0:
            raise ValidationError(_('Phone number should be a positive number'))

        return phone_number

    def save(self, request):
        user = super().save(request)

        country = self.cleaned_data['country']
        age = self.cleaned_data['age']
        phone_number = self.cleaned_data['phone_number']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        last_login_date = self.cleaned_data['last_login_date']
        role = self.cleaned_data['role']

        user.userprofile.country = country
        user.userprofile.age = age
        user.userprofile.phone_number = phone_number
        user.userprofile.first_name = first_name
        user.userprofile.last_name = last_name
        user.userprofile.last_login_date = last_login_date
        user.userprofile.role = role
        user.userprofile.save()

        return user
