# 은행계좌 클래스
class Account:
    # 속성(변수)
    __bank = None
    __id = None
    __name = None
    __money = 0

    # 생성자 정의
    def __init__(self, bank, id, name, money):
        self.__bank = bank
        self.__id = id
        self.__name = name
        self.__money = money

    # 기능(함수)
    def deposit(self, _money):
        self.__money += _money

    def withdraw(self, _money):
        self.__money -= _money

    def show(self):
        print('-------------------')
        print('은행명 :', self.__bank)
        print('계좌번호 :', self.__id)
        print('입금주 :', self.__name)
        print('현재잔액 :', self.__money)

