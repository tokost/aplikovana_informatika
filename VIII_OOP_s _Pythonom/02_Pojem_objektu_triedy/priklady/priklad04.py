# !!!! Self v pripade prveho parametru funkcie sa nemusi volat self
# ale moze byt pouzite akekolvek meno. Vacsinou sa vsak pouziva self

class Classroom2:
    def __init__(self, student_number):
        self.student_number = student_number

    def get_info(another_self):
        print(f"Cislo studenta je {another_self.student_number}")


new_class = Classroom2(20)
new_class.get_info()  # sa vnutorne prepise na
