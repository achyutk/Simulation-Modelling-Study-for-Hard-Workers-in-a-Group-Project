## Concentration against different Values of 'a' (Cost of Effort)
"""
*   We see test how different value of a (Cost of Effort) affect the concentration of hardworker and lazy worker in the population.
*   Keeping group_size constant 

"""
import School
import Visualisation

# Defining variables for the environment
population=10000
group_size = 5
years = 20
H_concentration=[] # List to store concentration value of hardworkers
L_concentration=[] # List to store concentration value of lazy workers
# Creating list of values for a
a_list=[x/100 for x in range(0,100)]

# Iterating over list of cost of effort
for a in a_list:
    
    school = School.School(population=population,group_size =group_size,a=a,years=years)


    H_concentration_a = [] # Temporary List to store concentration value of hardworkers
    L_concentration_a = [] # temporary List to store concentration value of lazy workers
    for i in range(years*2):
        school.get_group() # Assinging group
        school.get_marks() # Calculating marks
        Xh,Xl = school.concentration() # Calculating concentration of population
        H_concentration_a.append(Xh)
        L_concentration_a.append(Xl)
        school.update_strategy() # Updating strategy for next semester

    H_concentration.append(H_concentration_a)
    L_concentration.append(L_concentration_a)

Visualisation.multi_visualisation(years,a_list,H_concentration,L_concentration,numerical=False)
