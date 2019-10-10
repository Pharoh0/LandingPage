from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'second_name', 'E_mail', 'country', 'phone', 'phone_code','birthday', 'nationality',)
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'الاسم الاول'}),
            'second_name': forms.TextInput(attrs={'placeholder': 'الاسم الثاني'}),
            'E_mail': forms.EmailInput(attrs={'placeholder': 'joe@schmoe.com'}),

        }

