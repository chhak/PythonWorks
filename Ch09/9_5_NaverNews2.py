"""
날짜 : 2021/03/09
이름 : 김철학
내용 : 파이썬 가상 브라우저를 이용한 네이버 뉴스 수집
"""
from selenium import webdriver
from openpyxl import Workbook
from datetime import datetime

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('https://naver.com')

# 뉴스 클릭
btn_news = browser.find_element_by_css_selector('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2) > a')
btn_news.click()

# 속보 클릭
btn_sokbo = browser.find_element_by_css_selector('#lnb > ul > li:nth-child(2) > a')
btn_sokbo.click()


# Excel 파일생성
workbook = Workbook()
sheet = workbook.active

i = 0

while True:
    # 뉴스 리스트 제목 선택
    tags_dl = browser.find_elements_by_css_selector('#main_content > div.list_body.newsflash_body > ul > li > dl')

    # 뉴스 제목 출력
    for dl in tags_dl:

        try:
            title  = dl.find_element_by_css_selector('dt:nth-child(2) > a')
            writer = dl.find_element_by_css_selector('dd > span.writing')
            now    = "{:%Y-%m-%d}".format(datetime.now())

            sheet.append([writer.text, title.text.strip(), now])

        except:
            print('예외발생...')


    # 다음 페이지 번호 클릭
    tags_paging = browser.find_elements_by_css_selector('#main_content > div.paging > a')
    tags_paging[i].click()

    i += 1

    # 10번까지 제목 출력 후 종료
    if i > 8:
        break

# Excel 파일저장
workbook.save('C:/Users/bigdata/Desktop/News2.xlsx')
workbook.close()

# 브라우저 종료
browser.quit()