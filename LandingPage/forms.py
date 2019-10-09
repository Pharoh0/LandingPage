from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'E_mail', 'country', 'phone', 'phone_code','birthday', 'nationality',)