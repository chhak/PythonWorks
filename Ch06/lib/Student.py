from Ch06.lib.Person import Person

class Student(Person):

    __school = None
    __major = None

    def __init__(self, name, age, school, major):
        super().__init__(name, age)
        self.__school = school
        self.__major = major

    def hello(self):
        super().hello()
        print('학교 :', self.__school)
        print('전공 :', self.__major)

