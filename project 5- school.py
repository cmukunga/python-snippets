class Subject:
    def __init__(self, Student_name, Scores):
        self.Student_name = Student_name
        self.Scores = Scores

class Student:
    def __init__(self, student_id, Student_name, age):
        self.student_id = student_id
        self.Student_name = Student_name
        self.age = age
        self.Units = []

    def add_subject(self, subject):
        self.Units.append(subject)

    def get_total_Scores(self):
        return sum(subject.Scores for subject in self.Units)

class School:
    def __init__(self, Student_name):
        self.Student_name = Student_name
        self.students = []

    def New_Student(self, student):
        self.students.append(student)

    def Find_Student_Id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

# Usage example:
if __name__ == "__main__":
    unit1 = Subject("Communication Skills", 5)
    unit2 = Subject("Automata", 4)
    unit3 = Subject("Data Structure", 3)

    student1 = Student(1, "John Doe", 21)
    student1.add_subject(unit1)
    student1.add_subject(unit2)

    student2 = Student(2, "Jane Smith", 23)
    student2.add_subject(unit1)
    student2.add_subject(unit3)

    school = School("KYU University")
    school.New_Student(student1)
    school.New_Student(student2)

    # Find a student by ID and print their details and total Scores
    student_id_to_find = 1
    found_student = school.Find_Student_Id(student_id_to_find)
    if found_student:
        print(f"Student ID: {found_student.student_id}")
        print(f"Student_name: {found_student.Student_name}")
        print(f"Age: {found_student.age}")
        print(f"Total Scores: {found_student.get_total_Scores()}")
    else:
        print(f"Student with ID {student_id_to_find} not found in the school.")
