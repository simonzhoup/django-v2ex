from django import forms
from django.contrib.auth.models import User
from v2ex.models import UserProfile
from django.contrib.auth import authenticate, login, logout




class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, required=True, help_text='请使用半角的 a-z 或数字 0-9')
    email = forms.EmailField(label='邮箱', required=True, help_text='请使用真实电子邮箱注册，我们不会将你的邮箱地址分享给任何人')
    password = forms.CharField(label='密码', widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(label='重复密码', widget=forms.PasswordInput(), required=True, help_text='')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密码不一致')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.all().filter(email=email):
            raise forms.ValidationError('此邮箱已注册')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.all().filter(username=username):
            raise forms.ValidationError('用户名已存在')
        return username

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, required=True)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError('用户名/密码错误')



