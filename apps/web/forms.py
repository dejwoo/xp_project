from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.api.models import User


class SignUpForm(UserCreationForm):
    company = forms.CharField()

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'validate'}),
            'email': forms.EmailInput(attrs={'class': 'validate'}),
            'password1': forms.PasswordInput(attrs={'class': 'validate'}),
            'password2': forms.PasswordInput(attrs={'class': 'validate'}),
            'company': forms.TextInput(attrs={'class': 'validate'}),

        }
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.company = self.cleaned_data["company"]
        if commit:
            user.save()
        return user
