"""
날짜 : 2021/03/08
이름 : 김철학
내용 : 파이썬 네이버 뉴스 크롤링 실습
"""
import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

# 네이버 뉴스 요청하기
resp = req.get('https://news.naver.com/main/home.nhn', headers={'User-Agent': 'Mozilla/5.0'})
# print(resp.text)

# 헤드라인 뉴스 제목 5건 파싱
dom = bs(resp.text, 'html.parser')
tags_a = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')

for a in tags_a:
    print(a.text.strip())

# 네이버 속보 뉴스 크롤링
page = 1

# Excel 파일생성
workbook = Workbook()
sheet = workbook.active

while True:
    print('page :', page)
    url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20210308&page='+str(page)
    resp = req.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    dom = bs(resp.text, 'html.parser')

    tag_tits = dom.select('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:nth-child(2) > a')

    for tit in tag_tits:
        # print('tit : ', tit.text.strip())
        sheet.append([tit.text.strip()])

    page += 1

    if page > 10:
        break

# Excel 파일저장
workbook.save('C:/Users/bigdata/Desktop/News.xlsx')
workbook.close()

print('크롤링 완료...')



