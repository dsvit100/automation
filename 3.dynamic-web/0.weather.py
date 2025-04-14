from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
URL = 'https://weather.naver.com/compare/09470640'
driver.get(URL)

time.sleep(3)

weekly_weather = []

for i in range(7):
    weekly_date = driver.find_elements(By.CSS_SELECTOR, 'tr._cnCompareDay th div.time span.text')
    daily_low = driver.find_elements(By.CSS_SELECTOR, 'td div.inner_weather span.lowest')
    daily_high = driver.find_elements(By.CSS_SELECTOR, 'td span.lowest + span.temperature')

    date = weekly_date[i].text
    low = daily_low[i].text
    high = daily_high[i].text

    weekly_weather.append([date, low, high])

print(weekly_weather)
    





#weekly_weather = []
#weekly_dates = driver.find_elements(By.CSS_SELECTOR, 'th div.time span.text')
#daily_low = driver.find_elements(By.CSS_SELECTOR, 'td div.inner_weather span.lowest')
#daily_high = driver.find_elements(By.CSS_SELECTOR, 'td span.lowest + span.temperature')
#time.sleep(3)

#dates = [dates.text for date in weekly_dates]
#low = [daily_low.text for temperature in daily_low]
#high = [daily_high.text for temperature in daily_high]

#weekly_weather.append([dates, low, high])
#print(weekly_weather)

# weather_list = []

# for i in range(2):
#    weather_info[i].click()
#    time.sleep(2)
    
#    location = driver.find_element(By.CSS_SELECTOR, '')