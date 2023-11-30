from django import forms
from .models import CustomUser, Event, SpecialAnnouncement

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'username'}))
    User_ID = forms.CharField(widget=forms.TextInput(attrs={'class':'User_ID'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'first_name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'last_name'}))
    Phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'Phone_number'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'password2'}))
    
    class Meta:
        model = CustomUser
        fields = ['username','User_ID','first_name','last_name','Department','Phone_number'
                ,'email','password1', 'password2','Gender','is_superuser','is_staff']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return cleaned_data

class Announcement(forms.ModelForm):
    class Meta:
        model = SpecialAnnouncement
        fields = '__all__'


class EventsForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'