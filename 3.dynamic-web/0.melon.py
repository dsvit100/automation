# 1위부터 100위까지의 정보 수집

from selenium import webdriver
from selenium.webdriver.common.by import By
import time # 강제로 시간을 멈추는 코드
import csv # csv 파일을 열어보기 위해





driver = webdriver.Chrome()

URL = 'https://www.melon.com/chart/index.htm'
driver.get(URL)

# () 안의 기준점을 찾아줘야 하기 때문에 by를 import
# 태그를 찾기 위해 (CSS 속성을 기준으로, a태그인데, btn 안에 song_info 클래스가 들어있는 코드를 찾아줘)
song_info = driver.find_elements(By.CSS_SELECTOR, 'a.btn.song_info')
# 그 태그 중에서 title 요소를 꺼내줘 = print(song_info.get_attribute('title'))
#print(len(song_info))

song_list = []

for i in range(2):
    # song_info i번째에 접근
    song_info[i].click() # 클릭하고
    time.sleep(2) # 2초 기다려 - 내용 로딩이 필요하므로
    
    title = driver.find_element(By.CSS_SELECTOR, 'div.song_name').text # 이 element 안에 들어있는 text값만 가져오기
    artist = driver.find_element(By.CSS_SELECTOR, 'div.artist span').text # 'div.artist > a > span'
    # dd 태그들을 모두 가져온 후 인덱스 접근으로 필요한 정보 뽑아내기
    # meta_data = driver.find_elements(By.CSS_SELECTOR, 'div.meta dd') print(meta_data[1].text) 
    # 발매일 정보를 특정
    publish_date = driver.find_element(By.CSS_SELECTOR, 'dl.list > dd:nth-of-type(2)').text
    
    like_cnt = driver.find_element(By.CSS_SELECTOR, 'span#d_like_count').text
    like_cnt = like_cnt.replace(',', '')
    
    
    song_list.append([title, artist, publish_date, like_cnt])
    driver.back() # 뒤로가기


local_file_path = '/home/ubuntu/damf2/data/melon/'

# 작업이 다 끝난 후 csv로 저장헤주는 함수 만들기
def save_to_csv(song_list):
    
    # opne 파일 열기, 특정 위치에 내가 만들고 싶은 파일 이름을 작성
    # 'w' 쓰기로 파일 열기, encoding은 한글이 들어가 있기 때문에 옵션 설정해줌
    with open(local_file_path + 'melon-top-100.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(song_list) # song_list에 있는 노래 정보를 써줌
save_to_csv(song_list)