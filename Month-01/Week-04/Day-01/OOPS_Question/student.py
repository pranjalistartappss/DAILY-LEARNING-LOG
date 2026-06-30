class Students:
    def __init__(self,student_id, name, age, gender, class_name, section, roll_number, marks):

        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.class_name = class_name
        self.section = section
        self.roll_number = roll_number
        self.marks = marks
    
    def study(self):
        print(self.name, "is studying.")

    def attend_class(self):
        print(self.name, "is attending a class.")

    def take_exam(self):
        print(self.name, "is taking a exam.")
    
    def show_result(self):
        print("Marks:", self.marks)

    def show_profile(self):
        print("\n----- Student Profile -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Class:", self.class_name)
        print("Section:", self.section)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

student1 = Students(101, "Pranjali", 20, "Female", "B.Tech", "A", 45, 92)

# Call Methods
student1.show_profile()
student1.study()
student1.attend_class()
student1.take_exam()
student1.show_result()











# •	study()
# •	attend_class()
# •	take_exam()
# •	show_result()
# •	show_profile()
