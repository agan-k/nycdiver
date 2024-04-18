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
from selenium.webdriver.chrome.service import Service



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
    driver = webdriver.Chrome()
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
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return jQuery.active == 0"))
    list_results = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'listResults')))
    html = list_results.get_attribute('innerHTML')

    soup = BeautifulSoup(html, 'html.parser')
    upcoming_events = soup.find_all('div', 'eventsList-item')
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
        print(event)
    return
    for event in icp_dic:
        new_event = Event(
          owner='k-agan',
          headliner=event,
          cover_charge='No',
          cover_amount=icp_dic[event]['cover_amount'],
          date=icp_dic[event]['date'],
          time_start=icp_dic[event]['time_start'],
          time_end=icp_dic[event]['time_end'],
          venue='International Center of Photography',
          address_street='79 Essex Street',
          map_link='https://www.icp.org/',
          address_borough='Manhattan',
          description=icp_dic[event]['description'],
          cta=icp_dic[event]['cta'],
        )
        new_event.save()