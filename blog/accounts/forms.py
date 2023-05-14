from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationUserForm(UserCreationForm):
    email = forms.EmailField(help_text="Enter your email address", required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        
        return user
    


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'about_me', 'phone', 'sex', 'profile_image']

    
