import re
import requests
from bs4 import BeautifulSoup
from .models import Event
import datetime
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



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


icpURL = 'https://www.icp.org/events'

def get_icp(url):
    """Get visible events from the icpURL and save into Event instance"""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # Click all the popups
    cookies_popup = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'decline-cookies')))
    if cookies_popup is not None:
        cookies_popup.click()
    load_more_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'load_more')))
    load_more_btn.location_once_scrolled_into_view
    modal_popup = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mc-closeModal')))
    if modal_popup is not None:
        modal_popup.click()
    #Click 'View More' button for AJAX to bring in all the results
    load_more_btn.click()
    WebDriverWait(driver, 20).until(lambda driver: driver.execute_script("return jQuery.active == 0"))
    list_results = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'listResults')))
    html = list_results.get_attribute('innerHTML')
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
    upcoming_events = soup.find_all('div', 'eventsList-item')
    icp_dic = {}
    for e in upcoming_events:
        event = {}
        date_info = e.find('div', 'day')
        if date_info is not None:
            event_date = date_info.text.split()
            for i, word in enumerate(event_date):
                if i == 0:
                    day = word
                elif i == 1:
                    month = word
        event_date = str(current_year)+'-'+str(months[month])+'-'+str(day)
        event['date'] = event_date
        cta = e.find('a', 'eventsList-info')['href']
        event['cta'] = cta
        title = e.find('div', 'eventsList-eventTitle')
        event['headliner'] = title.text
        time = e.find('div', 'eventsList-eventHour')
        time = time.text.split(':')
        if 'PM' in time[1] and int(time[0]) < 12:
            time[0] = str(int(time[0]) + 12)
        elif int(time[0]) < 10:
            time[0] = '0' + str(time[0])
        
        
        time_end = str(int(time[0])+2)+':'+time[1]
        time_end = time_end.split(' ')
        time_start = str(time[0])+':'+time[1]
        time_start = time_start.split(' ')
        event['time_start'] = time_start[0]
        event['time_end'] = time_end[0]
        icp_dic[event['date']] = event
        # print(event)
    # print(icp_dic)
    for event in icp_dic:
        new_event = Event(
          owner='k-agan',
          headliner=icp_dic[event]['headliner'],
          cover_charge='N/A',
          cover_amount='',
          date=icp_dic[event]['date'],
          time_start=icp_dic[event]['time_start'],
          time_end=icp_dic[event]['time_end'],
          venue='International Center of Photography',
          address_street='79 Essex Street',
          map_link='',
          address_borough='Manhattan',
          description='',
          cta=icp_dic[event]['cta'],
        )
        new_event.save()