"""
날짜 : 2021/03/10
이름 : 김철학
내용 : 네이버 영화 리뷰 크롤링 실습
"""

from selenium import webdriver
from datetime import datetime
import time

# 크롬 가상 브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 영화 '미나리' 리뷰 페이지 이동
browser.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=187310&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false')

# 수집한 텍스트를 저장할 파일 생성
fname = './movie_review.txt'
file = open(fname, mode='w', encoding='utf8')

while True:
    # 영화 리뷰 수집하기
    try:
        tags_review = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li > div.score_reple > p > span > span > a')

        for tag in tags_review:
            tag.click()
    except:
        print('예외...')


    tags_span = browser.find_elements_by_css_selector('body > div > div > div.score_result > ul > li > div.score_reple > p > span:nth-child(2)')

    for span in tags_span:
        #print(span.text)
        file.write(span.text+'\n')

    # 다음 페이지 클릭
    try:
        next = browser.find_element_by_css_selector('body > div > div > div.paging > div > a:last-child > em')
        next.click()
    except:
        break


# 파일 닫기
file.close()

# 브라우저 종료
browser.quit()

print('프로그램 종료...')
