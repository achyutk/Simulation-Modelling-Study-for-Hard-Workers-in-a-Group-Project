import random
import School
import Visualisation


# Function to update the strategy for the second model
def update_strategy(school_composition,circle_size,a):
    number_of_groups = len(school_composition)//circle_size
    circle=[]
    for i in range(number_of_groups):
        circle=[(j,school_composition[j]) for j in range(len(school_composition)) if  school_composition[j].friend_group == i]
        
        for i in range(len(circle)):
            index, student = circle.pop(i)
            index2,random_student = random.choice(circle)
            circle.insert(i, (index,student))

            before_strategy = student.strategy
            payoff_student = student.marks - (a*student.strategy)
            payoff_randomstudent = random_student.marks - (a*random_student.strategy)        

            if payoff_randomstudent>payoff_student:
                imitation_chance = payoff_randomstudent-payoff_student
                if imitation_chance > 1:
                    imitation_chance = 1    

                imitation_strategy = random.choices([random_student.strategy,school_composition[i].strategy],weights=[imitation_chance,1-imitation_chance])
                school_composition[index].strategy = imitation_strategy[0]
#             print("Studentid:",student.student_id,"Studentgrp: ",student.friend_group,"Before: ",before_strategy,"- After:",student.strategy,"Friend: ","Friendid:",random_student.student_id,"Friendgrp: ",random_student.friend_group,"Friend Strategy: ",random_student.strategy)
    return school_composition

# Defining the variables
population=10000
group_size = 5
a=0.1
years = 100
circle_size=10

school = School.School(population=population,group_size =group_size,a=a,years=years,circle_size=circle_size)
school.get_friends()

H_concentration = [] # List to store concentration value of hardworkers
L_concentration = [] # List to store concentration value of lazy workers

#Iterating over semestes= years*2
for i in range(years*2):
    school.get_group() #Updating the group number of student
    school.get_marks() #Calculating marks of students
    Xh,Xl = school.concentration()  # Calculating concentration of the school
    H_concentration.append(Xh)
    L_concentration.append(Xl)
    school.school = update_strategy(school.school,circle_size,a) # Updating the strategy of student for next semester

Visualisation.visualisation(years,H_concentration,L_concentration)