from django.contrib.auth.models import User
from django.contrib.auth.password_validation import MinimumLengthValidator, NumericPasswordValidator, validate_password
from django import forms
from captcha.fields import CaptchaField
from .models import Post


class UserRegistration(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_conf = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserRegistration, self).clean()
        password = cleaned_data.get('password')
        conf_pass = cleaned_data.get('password_conf')

        if password != conf_pass:
            self.add_error(field='password_conf', error="Both Passwords don't match")

        validate_password(password=password)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','description','is_public']

        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter a title'
            }),

            'description': forms.Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Write your post',
            })
        }
