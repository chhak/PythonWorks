"""
날짜 : 2021/03/08
이름 : 김철학
내용 : 파이썬 웹 Request 실습하기
"""
import requests as req
from bs4 import BeautifulSoup as bs

# 네이버 요청
resp = req.get('https://naver.com')
# print(resp.text)

# 파싱(HTML문서에서 특정 데이터 추출)
dom = bs(resp.text, 'html.parser')
tag_a = dom.select_one('#yna_rolling > div:nth-child(1) > a')

print(tag_a.text)










