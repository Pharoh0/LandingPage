from django import forms
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.phonenumber import to_python

from .models import User



class UserForm(forms.ModelForm):

    #phone_number = PhoneNumberField()

    class Meta:
        NATIONALITY_CHOICES = (('1', 'خليجي'), ('2', 'ليس خليجي'))
        nationality = forms.Select(choices=NATIONALITY_CHOICES)
        #phone = PhoneNumberField()

        model = User

        fields = ('first_name', 'second_name', 'E_mail', 'country', 'phone', 'phone_code', 'age', 'nationality',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'الاسم الاول'}),
            'second_name': forms.TextInput(attrs={'placeholder': 'الاسم الثاني'}),
            'E_mail': forms.EmailInput(attrs={'placeholder': 'joe@schmoe.com'}),
            'nationality': forms.Select(choices=NATIONALITY_CHOICES, attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'الاسم الاول'}),

            #'phone': PhoneNumberField(attrs={'placeholder': 'enter phone'}),

        }

        def clean_national(self):
            nationality = self.cleaned_data['nationality']
            return nationality

        def clean_phone(self):
            phone = self.cleaned_data.get('phone_no', None)
            try:
                int(phone)
            except (ValueError, TypeError):
                raise ValidationError('Please enter a valid phone number')
            return phone

