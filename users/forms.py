<<<<<<< HEAD

from datetime import datetime
from captcha.fields import CaptchaField

=======
from cProfile import label
from datetime import datetime
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())
<<<<<<< HEAD
    captcha = CaptchaField(label='Введите текст с картинки')

=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
<<<<<<< HEAD
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))  # Добавлено form-control

=======
    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
    this_year = datetime.now().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-5))))

    class Meta:
        model = get_user_model()
<<<<<<< HEAD
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']
=======
        fields = ['photo','username', 'email', 'date_birth', 'first_name', 'last_name']
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
<<<<<<< HEAD
        widgets = {
=======
        widgets ={
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
<<<<<<< HEAD
=======
        # Проверяем, что email не занят другим пользователем
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
        if get_user_model().objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


<<<<<<< HEAD

=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))