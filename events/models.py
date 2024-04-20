from django.db import models
from django.urls import reverse
import uuid
from django.core.validators import MinLengthValidator



class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for Event')
    staged_for_deletion = models.BooleanField(default=False)
    owner = models.CharField('', max_length=50)
    headliner = models.CharField('name:', max_length=200)
    date = models.DateField('pick date:')
    time_start = models.TimeField('from:')
    time_end = models.TimeField('to:')
    venue = models.CharField('venue:', max_length=50)

    COVER_CHARGE = (
        ('No', 'No'),
        ('Yes', 'Yes'),
        ('N/A', 'N/A'),
    ) 

    cover_charge = models.CharField('cover charge?', null=True, max_length=16, default=None, choices=COVER_CHARGE)
    cover_amount = models.CharField('cover amount', null=True, blank=True, max_length=5)
    address_street = models.CharField('street address:', max_length=50)

    BOROUGHS = [
        ('', 'Choose Borough'),
        ('Brooklyn', 'Brooklyn'),
        ('The Bronx', 'The Bronx'),
        ('Queens', 'Queens',),
        ('Manhattan', 'Manhattan'),
        ('Staten Island', 'Staten Island'),
    ] 

    address_borough = models.CharField('borough', max_length=50, choices=BOROUGHS)
    address_zip = models.CharField('ZIP', max_length=5, blank=True)
    phone = models.CharField('phone:', max_length=10, null=True, blank=True, validators=[MinLengthValidator(10)])
    map_link = models.CharField('map link:', max_length=300, null=True, blank=True)
    description = models.CharField('notes:', blank=True, max_length=200)
    cta = models.CharField('cta link:', blank=True, max_length=200)

    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.date}, {self.headliner} {self.venue}'

      
