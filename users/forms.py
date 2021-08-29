from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Reviews


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'full_name', 'country', 'birthdate', 'start_date', 'end_date', 'details',)
        widgets = {
            'birthdate': DateInput(),
            'start_date': DateInput(),
            'end_date': DateInput()
            }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('start_date', 'end_date', 'details')

class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ('title', 'content', 'rating','pic')