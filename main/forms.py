from django import forms
from .models import Reservations

class ReservationForm(forms.ModelForm):
    def clean_name(self):
        user_name = self.data['name'].strip()
        return user_name.upper()


    class Meta:
        model = Reservations
        fields = ('name', 'email', 'phone', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'name': 'name',
                                           'id': 'name',
                                           'placeholder': "Ваше ім'я"}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'id': 'email',
                                             'name': 'email',
                                             'placeholder': 'Ваш Email',
                                             'data-rule': 'email',
                                             'data-msg': 'Please enter a valid email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control',
                                            'id': 'phone',
                                            'placeholder': '+38xxxxxxxxxx'}),

            'subject': forms.TextInput(attrs={'class': 'form-control',
                                              'name': 'subject',
                                              'placeholder': 'Напрямок',}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'name': "message",
                                             'rows': "6",
                                             'placeholder': "Ваше повідомлення"}),
        }
