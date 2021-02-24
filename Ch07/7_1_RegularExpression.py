"""
날짜 : 2021/02/24
이름 : 김철학
내용 : 파이썬 정규표현식 실습 교재 p192

정규표현식(Regular Expression)
 - 특정한 규칙을 갖는 문자열을 처리하기 위한 문법
 - 일반적으로 특정 문자 검색, 매칭 여부를 많이 처리
"""
import re
from re import findall, match


str1 = '1234 abc홍길동 ABC_555_6 이사도시'

# 숫자검색
print(findall('1234', str1))
print(findall('[0-9]', str1))
print(findall('[0-9]{3}', str1))
print(findall('[0-9]{3,}', str1))

# 문자열검색
print(findall('[가-힣]{3,}', str1))
print(findall('[a-z|A-Z]{3,}', str1))

str2 = 'test1abcABC 123mbc 45test'

print(findall('^test', str2))
print(findall('st$', str2))

# 단어 검색
str3 = 'test^홍길동 abc 대한*민국 123$tbc'

result = findall('\\w{3,}', str3)
print(result)

# 응용
jumin1 = '123456-3235678'
result1 = match('[0-9]{6}-[1-4][0-9]{6}', jumin1)

if result1:
    print('result1 결과 매칭')
else:
    print('result1 결과 매칭 안됨')

jumin2 = '123456-5235678'
result2 = match('[0-9]{6}-[1-4][0-9]{6}', jumin2)

if result2:
    print('result2 결과 매칭')
else:
    print('result2 결과 매칭 안됨')





