#Defining the class of student
class Student:
    def __init__(self, student_id, strategy, marks=None, group_id = None):
        self.student_id = student_id
        self.marks = marks
        self.strategy = strategy
        self.group_id = group_id
  
    def display(self):
        print(self.student_id,'------',self.marks, '------', self.strategy,'------',self.group_id)


