import re
import requests
from bs4 import BeautifulSoup
from .models import Event
from datetime import datetime
import datetime
import datetime

today = datetime.date.today()
current_year = today.year

today = datetime.date.today()
current_year = today.year

months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}
sets = {
    '3:00 PM': '15:00:00',
    '7:30 PM': '19:30:00',
    '9:00 PM': '21:00:00',
    '10:30 PM': '22:30:00',
    '12:00 AM': '24:00:00',
}

# smallsURL = 'https://www.smallslive.com/search/upcoming-ajax/'
smallsURL = 'https://www.smallslive.com'

def get_smalls(url):
    """Get featured shows from the calendar slider on the smalls 
    site and save them into Event instance"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    upcoming_shows = soup.find_all('div', 'sub-info')
    smalls_dic = {}
    for show in upcoming_shows:
        event = {
           'date': '',
           'venue': '',
           'cover_amount': '',
           'time_start': '',
           'time_end': '',
           'address_street': '',
           'description': '',
        }
        venue = show.find('div', 'venue')
        venue = re.sub('Live at ', '', venue.text)
        event['venue'] = venue
        if venue == 'Smalls':
            event['address_street'] = 'Smalls - 183 West 10 th Street, basement'
            event['cover_charge'] = '35'
        else: 
            event['address_street'] = 'Mezzrow - 163 West 10 th Street, basement'
            event['cover_charge'] = '20'
        time_infos = show.find_all('div', 'sets')
        for info in time_infos:
            if 'Sets' in info.text or 'From' in info.text:
                event['description'] = info.text
                if 'Sets' in info.text:
                    time = re.sub('Sets at ', '', info.text)
                else:
                    time = re.sub('From ', '', info.text)
                set_start = time[:8]
                if set_start.endswith(' '):
                  time_start = sets[set_start.strip()]
                else:
                  time_start = sets[set_start]
                if time_start == '15:00:00': 
                  time_end = '17:45:00'
                if time_start == '19:30:00': 
                  time_end = '21:30:00'
                if time_start == '22:30:00':
                  time_end = '23:30:00'
                event['time_start'] = time_start
                event['time_end'] = time_end
            else:
                date = info.text.split()
                for i, word in enumerate(date):
                    if i == 2:
                        day = word
                    elif i == 1:
                        month = word
                event_date = str(current_year)+'-'+str(months[month])+'-'+str(day)
                event['date'] = event_date
                
            smalls_dic[show.find('p', 'event-info-title').text] = event 

    for event in smalls_dic:
        new_event = Event(
          owner='k-agan',
          headliner=event,
          cover_charge='Yes',
          cover_amount=smalls_dic[event]['cover_charge'],
          date=smalls_dic[event]['date'],
          time_start=smalls_dic[event]['time_start'],
          time_end=smalls_dic[event]['time_end'],
          venue=smalls_dic[event]['venue'],
          address_street=smalls_dic[event]['address_street'],
          address_borough='Manhattan',
          description=smalls_dic[event]['description']
        )
        new_event.save()