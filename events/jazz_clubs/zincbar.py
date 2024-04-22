import requests
from bs4 import BeautifulSoup
from ..models import Event
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

zincbarURL = 'https://www.zincbar.com/shows/'

def get_zincbar(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    container = soup.find('div', 'offbeat-event-list-holder offbeat-event-list-standard edgtf-el-no-columns edgtf-normal-space')
    upcoming_shows = container.find_all('div', 'edgtf-el-item')
    zincbar_dic = {}
    for show in upcoming_shows:
        event = {}
        cta = show.find('a', 'edgtf-btn edgtf-btn-large edgtf-btn-solid edgtf-btn-orange-black edgtf-el-item-link')['href']
        event['cta'] = cta
        headliner = show.find('h4', 'edgtf-el-item-title')
        event['headliner'] = headliner.text.strip()
        day = show.find('span', 'edgtf-el-item-day').text.strip()
        month = show.find('span', 'edgtf-el-item-month').text.strip()
        event_date = str(current_year)+'-'+str(months[month])+'-'+str(day)
        event['date'] = event_date
        zincbar_dic[event['headliner']] = event

    for event in zincbar_dic:
        new_event = Event(
          owner='k-agan',
          headliner=event,
          cover_charge='Yes',
          cover_amount='25-45',
          date=zincbar_dic[event]['date'],
          time_start='19:00',
          time_end='22:00',
          venue='Zinc Bar',
          address_street='82 West 3rd Street',
          map_link='https://maps.app.goo.gl/waFeo7tH33JPZVob7',
          address_borough='Manhattan',
          description='',
          cta=zincbar_dic[event]['cta'],
        )
        new_event.save()