class Student:
    def __init__(self):
        self.__grade = None

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return f"{self.__grade}"


student1 = Student()
student1.set_grade('A')
print(student1.get_grade())
