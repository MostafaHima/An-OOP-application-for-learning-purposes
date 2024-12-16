class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def is_passing(self):
        return self.grade >= 50

    def get_info(self):
        check = "successful" if self.is_passing() else "Not Successful"
        print(f"""
        Name: {self.name}
        Age: {self.age}
        Grade: {self.grade}
        Stats = {check}
        """)


student1 = Student("Mohamed", 80, 20)
student2 = Student("Mostafa",100, 21)
student3 = Student("Yahya", 40, 18)
student4 = Student("Yousef", 33, 18)

# Display student one
student1.get_info()


# Display Student two
student2.get_info()


# Display Student Three
student3.get_info()


# Display Student Four
student4.get_info()

