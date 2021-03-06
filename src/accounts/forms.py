from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    # username = forms.CharField(length=100)
    email = forms.EmailField(required=True)

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs=({'required': ''})),
            'email': forms.EmailInput(attrs=({'required': ''})),
            'password1':forms.PasswordInput(attrs={'required': ''}),
            'password2':forms.PasswordInput(attrs={'required': ''}),

        }
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']

        if commit:
            user.save()
        
        return user