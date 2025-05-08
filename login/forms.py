from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="email",
        max_length=50
    )

    password = forms.CharField(
        label="password",
        max_length=128,
        widget=forms.PasswordInput()
    )
