
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Ім'я та Прізвище",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    phone = forms.CharField(
        label="Номер телефону",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    name_tovar = forms.CharField(
        label="Назва тавару",
        max_length=70,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    Problem_description = forms.CharField(
        label="Повідомлення",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Напишіть ваше повідомлення...'
        })
    )

    def clean_message(self):
        message = self.cleaned_data.get('Problem_description')
        if len(message) < 20:
            raise forms.ValidationError(
                "Повідомлення повинно містити хоча б 20 символів."
            )
        return message

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError(
                "Ім'я та прізвище повинні містити тільки літери."
            )
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError(
                "Номер телефону повинен містити тільки цифри."
            )
        return phone
