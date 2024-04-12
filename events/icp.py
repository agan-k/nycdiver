import re
import requests
from bs4 import BeautifulSoup
from .models import Event
from datetime import datetime
import datetime
import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


today = datetime.date.today()
current_year = today.year

today = datetime.date.today()
current_year = today.year

months = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12',
}
sets = {
    '5:00 pm': '17:00:00',
    '7:30 pm': '19:30:00',
    '8:00 pm': '20:00:00',
    '8:30 pm': '20:30:00',
    '10:00 pm': '22:00:00',
}

icpURL = 'https://www.icp.org/events'

def get_icp(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # wait = WebDriverWait(driver, 10)
    # load_more = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'View More')))
    load_more = driver.find_element('a', 'load_more')
    return print(load_more)
    driver.get('https://google.com')
    driver.find_element_by_id('load_more')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    upcoming_events = soup.find(id='listResults')
    return print(upcoming_events)
    upcoming_shows = soup.find_all('div', 'stm-schedule-item')
    icp_dic = {}
    for show in upcoming_shows:
        event = {
           'date': '',
           'venue': 'St. icp',
           'cover_amount': '15',
           'time_start': '',
           'time_end': '',
           'address_street': '345 Grand Street',
           'description': '',
           'cta': '',
        }
        cta = show.find('a', 'stm-book-here')['href']
        event['cta'] = cta
        content = show.find('div', 'stm-schedule-item-content').text
        content_lower = content.lower()
        content_text = content_lower.split()
        if 'private' in content_text:
            continue
        date = show.find('div', 'stm-schedule-item-date').text.split()
        for i, word in enumerate(date):
            if i == 2:
                day = word
            elif i == 1:
                month = word
        event_date = str(current_year)+'-'+str(months[month])+'-'+str(day)
        event['date'] = event_date
        time = show.find('div', 'stm-schedule-item-time').text
        set_start = time[:8]
        if set_start.endswith(' '):
            time_start = sets[set_start.strip()]
        else:
            time_start = sets[set_start]
        if time_start == '17:00:00': 
            time_end = '19:00:00'
        if time_start == '19:30:00': 
            time_end = '21:30:00'
        if time_start == '20:00:00':
            time_end = '22:00:00'
        if time_start == '20:30:00':
            time_end = '23:00:00'
        if time_start == '22:00:00':
            time_end = '23:50:00'
        event['time_end'] = time_end
        event['time_start'] = time_start

        icp_dic[content] = event

    for event in icp_dic:
        new_event = Event(
          owner='k-agan',
          headliner=event,
          cover_charge='Yes',
          cover_amount=icp_dic[event]['cover_amount'],
          date=icp_dic[event]['date'],
          time_start=icp_dic[event]['time_start'],
          time_end=icp_dic[event]['time_end'],
          venue=icp_dic[event]['venue'],
          address_street=icp_dic[event]['address_street'],
          map_link='https://www.sticp.com/',
          address_borough='Brooklyn',
          description=icp_dic[event]['description'],
          cta=icp_dic[event]['cta'],
        )
        new_event.save()