import re
import requests
from bs4 import BeautifulSoup
from .models import Event
from datetime import date, timedelta, datetime
import pytz
import datetime

today = datetime.date.today()
current_year = today.year

months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}

def get_page(url):
    print('vanguard')
    r = requests.get(url)
    # print (r.status_code)
    # with open("test.html", "w") as fp:
    #     fp.write(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    upcoming_events = soup('h4')
    for event in upcoming_events:
        event_headliner = event.contents[1]
        event_headliner = re.sub('</strong>', '', str(event_headliner))
        event_headliner = re.sub('<strong>', '', str(event_headliner))
        event_date = event.contents[0].split(' ')
        month = months[event_date[0]]
        day = event_date[1]
        event_date = str(month)+'/'+str(day)+'/'+str(current_year)
        
        print(soup.h4.string)
        # new_event = Event(
        #   owner='k-agan',
        #   headliner=event_headliner,
        #   date=event_date,
        #   time_start='20:00:00',
        #   time_end='23:00:00',
        #   venue='Village Vanguard',
        #   address_street='178 7TH Avenue South',
        #   address_borough='Manhattan'
        # )
        # new_event.save()

URL = 'https://villagevanguard.com/event/coming-soon'
      
      
# if __name__ == '__main__': 
#   url = 'https://villagevanguard.com/event/coming-soon'
#   get_page(url)