"""
날짜 : 2021/02/22
이름 : 김철학
내용 : 파이썬 특수함수 실습하기 교재 p129
"""

# 디폴트 매개변수
def hello(name='홍길동', age=21):
    print('이름 :', name)
    print('나이 :', age)


hello()
hello('김유신')
hello('김춘추', 25)

# 가변 매개변수
def total( *scores ):
    tot = 0
    for score in scores:
        tot += score

    return tot


r1 = total(1)
r2 = total(1, 2)
r3 = total(1, 2, 3)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

# 하나 이상의 리턴값
def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2

    return y1, y2


rs1, rs2 = sum_and_multi(2, 3)
print('rs1 :', rs1)
print('rs2 :', rs2)

# 변수에 저장하는 함수
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y


var1 = plus
var2 = minus

res1 = var1(2, 3)
res2 = var2(2, 3)

print('res1 :', res1)
print('res2 :', res2)

cal_list = [plus, minus]
res3 = cal_list[0](3, 4)
res4 = cal_list[1](4, 6)

print('res3 :', res3)
print('res4 :', res4)

# 람다함수
adder = lambda x, y: x + y
result = adder(2, 3)
print('result :', result)

# 연습문제
def gcd(n1, n2):
    temp = 0

    if n1 < n2:
        temp = n1
    else:
        temp = n2

    while True:

        if n1 % temp == 0 and n2 % temp == 0:
            break

        temp -= 1

    return temp


print('1과 5의 최대공약수 :', gcd(1, 5))
print('2과 6의 최대공약수 :', gcd(2, 6))
print('6과 9의 최대공약수 :', gcd(6, 9))
print('18과 12의 최대공약수 :', gcd(18, 12))
print('60과 24의 최대공약수 :', gcd(60, 24))




