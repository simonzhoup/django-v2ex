from django import forms
from django.contrib.auth.models import User
from v2ex.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(label='用户名', max_length=20, required=True)
    email = forms.EmailField(label='邮箱', required=True)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(label='重复密码', widget=forms.PasswordInput(), required=True)

    def clean(self):
        data = super(UserForm, self).clean()
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise forms.ValidationError('两次密码不一致')
