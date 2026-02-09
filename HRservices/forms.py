from django import forms
from .models import Application, ContactMessage
from HRservices import models

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # all fields required
        for field in self.fields.values():
            field.required = True


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    class Meta:
        model=models.Service
        fields='__all__'

