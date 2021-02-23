from Ch06.lib.Student import Student

class SalaryStudent(Student):

    __company = None

    def __init__(self, name, age, school, major, company):
        super().__init__(name, age, school, major)
        self.__company = company

    def hello(self):
        super().hello()
        print('회사 :', self.__company)
