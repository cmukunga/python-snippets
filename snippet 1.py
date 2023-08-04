class Student:
    def __init__(self, first_name, second_name, reg, course, grade):
        self.first_name = first_name
        self.second_name = second_name
        self.reg = reg
        self.course = course
        self.grade = grade

    def Registration(self):
        print(
            f"Student details : \nName: {self.first_name} {self.second_name}.\nReg_no: {self.reg}.\nCourse: {self.course}.\nMean Grade: {self.grade}."
        )

if __name__ == "__main__":
    student1 = Student("John", "Tosh", "PA22ED45", "Computer Science", "pass")
    student1.Registration()

