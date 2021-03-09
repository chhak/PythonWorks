"""
날짜 : 2021/03/09
이름 : 김철학
내용 : 파이썬 날씨 데이터 크롤링 실습
"""
from selenium import webdriver
import pymysql

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

trs = browser.find_elements_by_css_selector('#weather_table > tbody > tr')

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='chhak',
                       password='1234',
                       db='chhak',
                       charset='utf8')

# SQL 실행객체 생성
cursor = conn.cursor()

for tr in trs:
    city     = tr.find_element_by_css_selector('td > a').text
    visible  = tr.find_element_by_css_selector('td:nth-child(3)').text
    temp     = tr.find_element_by_css_selector('td:nth-child(6)').text
    dew      = tr.find_element_by_css_selector('td:nth-child(7)').text
    feel     = tr.find_element_by_css_selector('td:nth-child(8)').text
    humidity = tr.find_element_by_css_selector('td:nth-child(11)').text
    wind_direct = tr.find_element_by_css_selector('td:nth-child(12)').text
    wind_speed  = tr.find_element_by_css_selector('td:nth-child(13)').text
    sea         = tr.find_element_by_css_selector('td:nth-child(14)').text
    # print(city, visible, temp, dew, feel, humidity, wind_direct, wind_speed, sea)
    # SQL 실행
    sql  = "INSERT INTO `Weather` SET "
    sql += "`city`='"+city+"',"
    sql += "`visible`='"+visible+"',"
    sql += "`temp`='"+temp+"',"
    sql += "`dew`='"+dew+"',"
    sql += "`feel`='"+feel+"',"
    sql += "`humidity`='"+humidity+"',"
    sql += "`wind_direct`='"+wind_direct+"',"
    sql += "`wind_speed`='"+wind_speed+"',"
    sql += "`sea`='"+sea+"',"
    sql += "`rdate`=NOW();"

    cursor.execute(sql)
    conn.commit()

    print('수집 중...')

# 데이터베이스 종료
conn.close()

# 가상 브라우저 종료
browser.quit()

print('수집완료...')
