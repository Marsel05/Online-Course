from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import UserProfile


class CustomSignupForm(SignupForm):
    country = forms.CharField(max_length=100, label=_('Country'), required=False)
    age = forms.IntegerField(label=_('Age'), required=False)
    phone_number = forms.CharField(max_length=20, label=_('Phone Number'), required=False)
    first_name = forms.CharField(max_length=100, label=_('First Name'), required=False)
    last_name = forms.CharField(max_length=100, label=_('Last Name'), required=False)
    last_login_date = forms.DateField(label=_('Last Login Date'), required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if phone_number and (len(phone_number) != 9 or not phone_number.isdigit()):
            raise ValidationError(_('Invalid phone number format. Please use a 9-digit format without spaces'))

        return phone_number

    def save(self, request):
        user = super().save(request)

        country = self.cleaned_data.get('country')
        age = self.cleaned_data.get('age')
        phone_number = self.cleaned_data.get('phone_number')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        last_login_date = self.cleaned_data.get('last_login_date')

        if hasattr(user, 'userprofile'):
            profile = user.userprofile
        else:
            profile = UserProfile(user=user)

        profile.country = country
        profile.age = age
        profile.phone_number = phone_number
        profile.first_name = first_name
        profile.last_name = last_name
        profile.last_login_date = last_login_date
        profile.save()

        return user
