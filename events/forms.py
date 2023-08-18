from django import forms
from django.forms import ModelForm
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
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
            'headliner': forms.TextInput(attrs={'class': 'form-input'}),
            'venue': forms.TextInput(attrs={'class': 'form-input'}),
            'cover_charge': forms.RadioSelect(attrs={'class': 'cover-charge', 'onchange': 'displayCoverAmountInput(this.value);'}),
            'cover_amount': forms.TextInput(attrs={'class': 'form-input cover-amount'}),
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
        address_zip = cleaned_data.get('address_zip')
        cover_amount = cleaned_data.get('cover_amount')
        map_link = cleaned_data.get('map_link')

        if date < date.today():
            self.add_error('date', 'Invalid date - Event listing in the past')
        if time_end < time_start:
            self.add_error('time_end', 'Invalid time - End Time before Start Time')
        if cover_amount is not None:
            if not cover_amount.isdigit():
                self.add_error('cover_amount', 'Invalid amount - Enter enter amount number')
        if address_zip is not None:
            if len(address_zip) < 5 or not address_zip.isdigit():
                self.add_error('address_zip', 'Invalid ZIP code - Enter 5-digit number')
        if map_link is not None:
            if 'https://' not in map_link and 'http://' not in map_link:
                self.add_error('map_link', 'Invalid map URL - URL should start with http:// or https://')
        return cleaned_data