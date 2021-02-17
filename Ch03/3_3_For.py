"""
날짜 : 2021/02/17
이름 : 김철학
내용 : 파이썬 반복문 For 실습 교재 p70
"""

# for문
for i in range(10):
    print('i :', i)

for i in range(10, 20):
    print('i :', i)

for i in range(10, 0, -1):
    print('i :', i)

# 1부터 10까지 합
sum1 = 0

for k in range(11):
    sum1 += k

print('1부터 10까지 합 : %d' % sum1)

# 1부터 10까지 짝수 합
sum2 = 0

for k in range(11):

    if k % 2 == 0:
        sum2 += k

print('1부터 10까지 짝수 합 : %d' % sum2)

# 이중 for문
for a in range(3):
    print('a :', a)
    for b in range(5):
        print('b :', b)

# 구구단
for x in range(2, 10):

    print('%d단' % x)
    for y in range(1, 10):

        z = x * y
        print('%d x %d = %d' % (x, y, z))


# 별삼각형
for a in range(10, 0, -1):

    for b in range(a):
        print('☆', end=',')

    print('')


for i in range(10):
    print('★,' * i)


# 리스트를 이용한 for문
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print('num :', num)

for person in ['김유신', '김춘추', '장보고']:
    print('person :', person)

scores = [62, 86, 72, 74, 96]
total = 0

for score in scores:
    total += score

print('점수 합 :', total)

# 튜플를 이용한 for문
nums = (10, 20, 30, 40, 50)

for n in nums:
    print('n :', nums)

for animal in ('사자', '호랑이', '독수리'):
    print('animal :', animal)
