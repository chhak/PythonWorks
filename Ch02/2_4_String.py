"""
날짜 : 2021/02/15
이름 : 김철학
내용 : 파이썬 문자열(String) 연산 실습하기
"""

# 문자열 더하기
str1 = 'Hello'
str2 = 'Python'

result = str1 + str2
print('result :', result)

# 문자열 곱하기
name = '홍길동'
print('name * 3 :', name*3)

# 문자열 길이
msg = 'Hello World'
print('msg 길이 :', len(msg))

# 문자열 인덱스
print('msg의 1번째 문자 :', msg[0])
print('msg의 7번째 문자 :', msg[6])
print('msg의 마지막 문자 :', msg[-1])

# 문자열 슬라이스
# 문자열 분리
# 문자열 포멧