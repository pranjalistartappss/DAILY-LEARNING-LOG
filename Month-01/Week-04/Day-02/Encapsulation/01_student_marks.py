class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 5 <= age <= 25:
            self.__age = age
        else:
            print("Invalid Age")

    def show_details(self):
        print("Name :", self.__name)
        print("Age :", self.__age)


student = Student("Rahul", 20)
student.show_details()
student.set_age(22)
print()
student.show_details()