import School
import Visualisation

# Initialisation
population=10000
group_size = 5
a=0.1
years = 50
school = School.School(population=population,group_size =group_size,a=a,years=years)

# List of concentration 
H_concentration = [] # List to store concentration value of hardworkers
L_concentration = [] # List to store concentration value of lazy workers


#Iterating over semestes= years*2
for i in range(years*2):
    
    school.get_group() #Updating the group number of student
    school.get_marks() #Calculating marks of students
    Xh,Xl = school.concentration() # Calculating oncentration of the school
    H_concentration.append(Xh)
    L_concentration.append(Xl)
    school.update_strategy() # Updating the strategy of student for next semester

# Visualisitng the concentration over different semesters
Visualisation.visualisation(years,H_concentration,L_concentration)



