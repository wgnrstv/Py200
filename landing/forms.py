from django import forms


class LoginForm(forms.Form):
    my_text = forms.CharField(label='', max_length=100)
    email = forms.EmailField(label='email')

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
