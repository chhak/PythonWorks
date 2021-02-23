"""
날짜 : 2021/02/23
이름 : 김철학
내용 : 파이썬 클래스 상속 실습하기 교재 p163
"""
from Ch06.lib.StockAccount import StockAccount
from Ch06.lib.Student import Student
from Ch06.lib.SalaryStudent import SalaryStudent

kb = StockAccount('KB증권', '101-12-1234', '김유신', 50000, '삼성전자', 10, 40000)
kb.deposit(50000)
kb.withdraw(4000)
kb.buy('삼성전자', 5, 45000)
kb.sell('삼성전자', 5, 50000)
kb.show()

kim = Student('김춘추', 24, '부산대', '영문과')
kim.hello()

lee = SalaryStudent('이순신', 31, '부경대', '경영학', '삼성전자')
lee.hello()