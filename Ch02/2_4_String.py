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
str = 'Hello Korea'

print('str[0:5] :', str[0:5])
print('str[6:11] :', str[6:11])
print('str[:5] :', str[:5])
print('str[6:] :', str[6:])

# 문자열 분리
people = '김유신|김춘추|장보고|강감찬|이순신'

p1, p2, p3, p4, p5 = people.split('|')

print('p1 :', p1)
print('p2 :', p2)
print('p3 :', p3)
print('p4 :', p4)
print('p5 :', p5)

# 문자열 포맷
fstr1 = '%d월 %d일'
fstr2 = '%d월 %d일 %s요일'

print(fstr1 % (2, 16))
print(fstr2 % (2, 16, '화'))


