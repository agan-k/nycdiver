import re
import requests
from bs4 import BeautifulSoup
from .models import Event
from datetime import datetime
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

def get_vanguard(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    upcoming = soup.find('div', 'event-short-description')
    # remove spaces between html tags:
    para = re.sub(">\s*<","><", str(upcoming.p))
    upcoming_events = BeautifulSoup(para, 'html.parser')
    upcoming_events = upcoming_events.p
    events_dic = {}
    for child in upcoming_events.children:
        if child.name == 'h4':
            event_date = child.contents[0].split(' ')
            month = months[event_date[0]]
            day = event_date[1]
            event_date = str(current_year)+'-'+str(month)+'-'+str(day)
            event = {
                'date': event_date
            }
            events_dic[child.strong.contents[0]] = event
            for sibling in child.next_siblings:
                if sibling.name == 'p':
                    event['description'] = sibling.string
                    #check if there's another <p> with additional description and then give up! :^\
                    for adjacent_sib in sibling.next_siblings:
                        if adjacent_sib and adjacent_sib.name == 'p':
                            event['description'] += ', '+adjacent_sib.string
                        break
                break

    for event in events_dic:
        new_event = Event(
          owner='k-agan',
          headliner=event,
          cover_charge='Yes',
          cover_amount='40',
          date=events_dic[event]['date'],
          time_start='20:00:00',
          time_end='23:00:00',
          venue='Village Vanguard',
          address_street='178 7TH Avenue South',
          address_borough='Manhattan',
          description=events_dic[event]['description']
        )
        new_event.save()

URL = 'https://villagevanguard.com/event/coming-soon'
      
      
# if __name__ == '__main__': 
#   url = 'https://villagevanguard.com/event/coming-soon'
#   get_page(url)