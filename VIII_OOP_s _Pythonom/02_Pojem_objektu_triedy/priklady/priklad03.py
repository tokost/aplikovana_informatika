class Classroom:
    def __init__(self, student_number):
        self.student_number = student_number

    def get_info(self):
        print(f"Cislo studenta je {self.student_number}")


new_class = Classroom(10)
new_class.get_info()
Classroom.get_info(new_class)
