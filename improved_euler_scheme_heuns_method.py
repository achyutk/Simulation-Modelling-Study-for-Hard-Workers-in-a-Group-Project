## Improved Euler Scheme- Heun's Method

import School
import Visualisation

# Defining f(x) which is the slope
def f(Xh,group_size,a):
    return Xh*(1-Xh)*(1/group_size-a)


"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
## Improved Euler Scheme with one step size

# Initialising the variables
Xh=0.5
years = 500
group_size=7
a=0.2

H_concentration = [] # List to store concentration value of hardworkers
H_concentration.append(Xh)

h = 1
# Iterating over time intervals
for i in range(years*2):
    K1 =  h * f(H_concentration[-1],group_size,a) # Euler method of predition
    K2 = h * f(H_concentration[-1] + K1,group_size,a) # Refined Prediction
    Xh_next = H_concentration[-1] + 0.5*(K1+K2) # Estimating next value using Heun's method
    H_concentration.append(Xh_next)
L_concentration = [1-x for x in H_concentration] # List to store concentration value of lazy workers

Visualisation.visualisation(years,H_concentration[:-1],L_concentration[:-1])    #Visualising the concentration over the years

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
## Improved Euler Scheme with multiple step size


# Solving The equation using multiple step size
h_list=[50,25,1,0.1,0.01]

H_overall_concentration=[] # List to store concentration value of hardworkers
L_overall_concentration=[] # List to store concentration value of lazy workers

# Iterating over different values of step size
for h in h_list: 
    # Defining the variables
    Xh=0.5
    years = 500
    group_size=7
    a=0.2

    H_concentration = [] # Temproary List to store concentration value of hardworkers
    H_concentration.append(Xh)
    
    #Iterating over different intervals
    for i in range(years*2):
        K1 =  h * f(H_concentration[-1],group_size,a) # Euler method of predition
        K2 = h * f(H_concentration[-1] + K1,group_size,a) # Refined Prediction
        Xh_next = H_concentration[-1] + 0.5*(K1+K2) # Estimating next value using Heun's method
        H_concentration.append(Xh_next)

    L_concentration = [1-x for x in H_concentration] # Temproary List to store concentration value of lazyworkers
    H_overall_concentration.append(H_concentration)
    L_overall_concentration.append(L_concentration)

Visualisation.multi_visualisation(years,h_list,H_overall_concentration,L_overall_concentration,numerical=True)