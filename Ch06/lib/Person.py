class Person:

    __name = None
    __age = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def hello(self):
        print('---------------')
        print('이름 :', self.__name)
        print('나이 :', self.__age)

