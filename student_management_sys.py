class Student:
    def __init__(self,name,student_id,course):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.scores = []
    
    def add_score(self,score):
        if (score <= 100) and (score >= 0) and not isinstance(score,str):
            self.scores.append(score)
    
    def calculate_average(self):
        total_calculation = 0
        if len(self.scores) != 0:
            for i in self.scores:
                total_calculation = total_calculation + i
            average = total_calculation / len(self.scores)
            return average
        else:
            return None
    
    def display_profile(self):
        print(self.name)
        print(self.student_id)
        print(self.course)
        print(self.calculate_average())
    


student_1 = Student("Prince",1825622,"Math")
student_1.add_score(10)
student_1.add_score(20)
student_1.add_score(30)

student_2 = Student("Edwin",1355223, "English")
student_2.add_score(20)
student_2.add_score(45)
student_2.add_score(100)
student_2.add_score(23)


student_1.display_profile()
student_2.display_profile()