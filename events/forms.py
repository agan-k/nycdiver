from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from .models import Event
import datetime


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'owner', 
            'headliner', 
            'venue', 
            'cover_charge', 
            'cover_amount', 
            'date', 
            'time_start', 
            'time_end',
            'address_street', 
            'address_borough', 
            'address_zip', 
            'phone',  
            'map_link', 
            'description',
        )
        widgets = {
            'owner': forms.TextInput(attrs={'type': 'hidden'}),
            'headliner': forms.TextInput(attrs={'class': 'form-input'}),
            'venue': forms.TextInput(attrs={'class': 'form-input'}),
            'cover_charge': forms.RadioSelect(attrs={'class': 'cover-charge', 'onchange': 'displayCoverAmountInput(this.value);'}),
            'cover_amount': forms.TextInput(attrs={'class': 'form-input cover-amount' ,'pattern':'[0-9]+'}),
            'date': forms.DateInput(attrs={'type':'date', 'class': 'form-input date-select'}),
            'time_start': forms.TimeInput(attrs={'class':'form-input', 'type':'time'}),
            'time_end': forms.TimeInput(attrs={'class':'form-input', 'type':'time'}),
            'address_street': forms.TextInput(attrs={'class':'form-input'}),
            'address_borough': forms.Select(attrs={'class':'form-input address-borough'}),
            'address_zip': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'pattern':'[0-9]+'}),
            'map_link': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input description', 'maxlength': '200',}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time_start = cleaned_data.get('time_start')
        time_end = cleaned_data.get('time_end')

        if date < date.today():
            self.add_error('date', 'Invalid date - Event listing in the past')
        if time_end < time_start:
            self.add_error('time_end', 'Invalid time - End Time before Start Time')

        return cleaned_data