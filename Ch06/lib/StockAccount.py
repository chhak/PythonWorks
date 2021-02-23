from Ch06.lib.Account import Account

class StockAccount(Account):

    __stock = None
    __amount = 0
    __price = 0

    def __init__(self, bank, id, name, money, stock, amount, price):
        super().__init__(bank, id, name, money)
        self.__stock = stock
        self.__amount = amount
        self.__price = price

    def buy(self, stock, amount, price):
        self.__stock = stock
        self.__amount += amount
        self.__price = price

    def sell(self, stock, amount, price):
        self.__stock = stock
        self.__amount -= amount
        self.__price = price

    def show(self):
        super().show()
        print('주식종목 :', self.__stock)
        print('주식수량 :', self.__amount)
        print('주식가격 :', self.__price)
