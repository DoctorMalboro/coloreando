from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    color = forms.CharField(max_length=7)