class Student:
    def _init_(self, name, score):
        self.name = name
        self.score = score

class GradeBook:
    def _init_(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        if len(self.students) == 0:
            return 0
        total = 0
        for student in self.students:
            total += student.score
        average = total / len(self.students)
        return average

student1 = Student("Collin", 89)
student2 = Student("Laureen", 90)
student3 = Student("Jeff", 95)

gradebook1 = GradeBook()
gradebook1.add_student(student1)
gradebook1.add_student(student2)
gradebook1.add_student(student3)

print("Class average:", gradebook1.get_average())