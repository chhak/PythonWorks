"""
날짜 : 2021/02/23
이름 : 김철학
내용 : 파이썬 클래스 실습하기 교재 p148
"""

from Ch06.lib.Account import Account

# Account 객체생성
kb = Account()

# 객체 멤버변수 초기화
kb.bank = '국민은행'
kb.id = '121-11-1021'
kb.name = '김유신'
kb.money = 10000

# 객체 기능활용
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

# 객체생성 및 초기화
wr = Account()
wr.bank = '우리은행'
wr.id = '111-12-1010'
wr.name = '김춘추'
wr.money = 30000

wr.deposit(10000)
wr.withdraw(20000)
wr.show()



