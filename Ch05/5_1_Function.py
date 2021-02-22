"""
날짜 : 2021/02/22
이름 : 김철학
내용 : 파이썬 함수 실습하기 교재 p114
"""
# 함수 : 일련의 코드로직을 모듈화 한 코드블럭
def ft(x):
    y = 2 * x + 3
    return y


def f(x):
    y = x**2 + x * 2 + 3
    return y


# 함수실행(호출)
rs1 = ft(1)
rs2 = ft(2)
rs3 = ft(3)

print('rs1 :', rs1)
print('rs2 :', rs2)
print('rs3 :', rs3)

print('f(1) :', f(1))
print('f(2) :', f(2))
print('f(3) :', f(3))

# 함수유형 1 - 매개변수 O, 리턴값 O
def type1(x, y):
    z = x + y
    return z


r1 = type1(1, 2)
r2 = type1(2, 3)

print('r1 :', r1)
print('r2 :', r2)

# 함수유형 2 - 매개변수 O, 리턴값 x
def type2(items):
    tot = 0
    for item in items:
        tot += item

    print('items 합 :', tot)


type2([1, 2, 3, 4, 5])
type2((1, 3, 5, 7, 9))
type2((2, 4, 6, 8, 10))


# 함수유형 3 - 매개변수 x, 리턴값 O
def type3():
    tot = 0
    for i in range(11):
        tot += i

    return tot


result = type3()
print('result :', result)

# 함수유형 4 - 매개변수 x, 리턴값 x
def type4():
    result = type3()
    print('type4 result :', result)

type4()

# 연습문제
def gugudan( num ):
    print('%d단' % num)

    for k in range(1, 10):
        print('%d x %d = %d' % (num, k, num * k))


for i in range(2, 10):
    gugudan(i)









