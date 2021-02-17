"""
날짜 : 2021/02/17
이름 : 김철학
내용 : 파이썬 조건문 실습 교재 p60
"""

# if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')


if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')


if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다.')


# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    """조건이 참 일때"""
    print('num3이 num4보다 크다.')
else:
    """조건이 거짓 일때"""
    print('num3이 num4보다 작다.')


# if ~ elif ~ else

if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

# 연습문제

score = input('점수 입력 : ')
score = int(score)  # 숫자변환

if score >= 90 and score <= 100:
    """ 90 ~ 100 """
    print('A 입니다.')
elif score >= 80 and score < 90:
    """ 80 ~ 89 """
    print('B 입니다.')
elif 70 <= score < 80:
    """ 70 ~ 79 """
    print('C 입니다.')
elif 60 <= score < 70:
    """ 60 ~ 69 """
    print('D 입니다.')
else:
    """ 0 ~ 59 """
    print('F 입니다.')

print('score :', score)

#교재 p63 삼항조건문