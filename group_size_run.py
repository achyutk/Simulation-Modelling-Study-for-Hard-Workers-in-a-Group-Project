## Concentration against different Values of 'group_size'
"""
*   We see test how different value of group_size affect the concentration of hardworker and lazy worker in the population.   
*   We have kept 'a' constant
"""

import School
import Visualisation


# Assiging values to the environment
population=10000
a = 0.5
years = 20
H_concentration=[] # List to store concentration value of hardworkers
L_concentration=[] # List to store concentration value of lazy workers
# Creating a list of values for group_size
group_size_list=[x for x in range(2,101)]

# Iterating over different values of group size
for group_size in group_size_list:

    school = School.School(population=population,group_size =group_size,a=a,years=years)
    H_concentration_a = [] # Temporary List to store concentration value of hardworkers
    L_concentration_a = [] # Temporary List to store concentration value of lazy workers
    
    # Iterating over semester
    for i in range(years*2):
        school.get_group() # Assinging group
        school.get_marks() # Calculating marks
        Xh,Xl = school.concentration() # Calculating concentration of population
        H_concentration_a.append(Xh)
        L_concentration_a.append(Xl)
        school.update_strategy() # Updating strategy for next semester
  
    H_concentration.append(H_concentration_a)
    L_concentration.append(L_concentration_a)

Visualisation.multi_visualisation(years,group_size_list,H_concentration,L_concentration,numerical=False)