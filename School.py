#Importing necessary packages
import random
import Student

#Defining the class of student
class School:
    def __init__(self,population,group_size,a,years):
        self.group_size = group_size
        self.a = a
        self.years = years 
        self.population = population
        self.strategy_composition = [random.choices([0,1])[0] for j in range(self.population)]
        self.school = [Student.Student(student_id = j,strategy= self.strategy_composition[j]) for j in range(self.population)]

    # Shuffling the students to assign group
    def get_group(self):
        random.shuffle(self.school)
        for i in range(self.population):
            self.school[i].group_id = i//self.group_size
        # return self.school
    
    # Function to calculate marks
    def get_marks(self):
        for i in range(0,self.population,self.group_size):    
            group=[]
            if(i!=(self.population-self.group_size)):
                group = self.school[i:i+self.group_size]
            else:
                group = self.school[i:]
            marks = sum([j.strategy for j in group])/self.group_size

            for j in range(i,i+len(group)):
                self.school[j].marks = marks
        # return self.school
    
    # Calculating Concentration of Students
    def concentration(self):
        Nh = 0
        Nl = 0
        for i in range(len(self.school)):
            if self.school[i].strategy==1:
                Nh = Nh+1
            else:
                Nl = Nl+1
    
        return Nh/len(self.school), Nl/len(self.school)

    def update_strategy(self):
        for i in range(len(self.school)):
            student = self.school.pop(i)
            random_student = random.choice(self.school)
            self.school.insert(i, student)

            payoff_student = self.school[i].marks - (self.a*self.school[i].strategy)
            payoff_randomstudent = random_student.marks - (self.a*random_student.strategy)

            if payoff_randomstudent>payoff_student:
                imitation_chance = payoff_randomstudent-payoff_student
                if imitation_chance > 1:
                    imitation_chance = 1    

                imitation_strategy = random.choices([random_student.strategy,self.school[i].strategy],weights=[imitation_chance,1-imitation_chance])
                self.school[i].strategy = imitation_strategy[0]

        # return self.school
