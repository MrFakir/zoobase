from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

from .models import Stigmas


class AddStigmaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_animal'].empty_label = 'Не выбрано'
        self.fields['sex'].empty_label = 'Не выбрано'
        self.fields['type'].empty_label = 'Не выбрано'

    class Meta:
        model = Stigmas
        fields = ['type', 'number', 'tag_number', 'type_animal', 'sex', 'the_pet', 'master', 'phone_number',
                  'description']

        widgets = {
            'number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': model.number.field.verbose_name}),
            'tag_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': model.tag_number.field.verbose_name}),
            'phone_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': model.phone_number.field.verbose_name}),
            'master': forms.TextInput(attrs={'class': 'form-control', 'placeholder': model.master.field.verbose_name}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': model.type.field.verbose_name}),
            'type_animal': forms.Select(
                attrs={'class': 'form-control', 'placeholder': model.type_animal.field.verbose_name}),
            'sex': forms.Select(attrs={'class': 'form-control', 'placeholder': model.sex.field.verbose_name}),
            'the_pet': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'placeholder': model.the_pet.field.verbose_name}),

            'description': forms.Textarea(
                attrs={'style': 'height: 100px', 'cols': 60, 'rows': 10, 'class': 'form-control',
                       'placeholder': model.description.field.verbose_name}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', }))


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ''}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': ''}),

        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count():
            raise ValidationError('Такой Email уже есть')

        return email
