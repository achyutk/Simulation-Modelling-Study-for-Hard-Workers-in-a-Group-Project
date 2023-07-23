import School
import Visualisation

# Defining f(x) which is the slope
def f(Xh,group_size,a):
    return Xh*(1-Xh)*(1/group_size-a)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
## Euler Scheme with one step size

# Initialising the variables
Xh=0.5
a=0.2
years = 500
group_size=7

H_concentration = [] # List to store concentration value of hardworkers
H_concentration.append(Xh)

h = 1   #Step size
#iterating over different intervals
for i in range(years*2):
    Xh_next = H_concentration[-1] + h*f(H_concentration[-1],group_size,a) #Estinmating Next X value using euler scheme
    H_concentration.append(Xh_next)
L_concentration = [1-x for x in H_concentration] # List to store concentration value of lazy workers

Visualisation.visualisation(years,H_concentration[:-1],L_concentration[:-1])    #Visualising the concentration over the years


"""------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
## Euler Scheme with multiple step size


# Solving The equation using multiple step_sizes
h_list=[50,25,1,0.1,0.01]

H_overall_concentration=[] # List to store concentration value of hardworkers
L_overall_concentration=[] # List to store concentration value of lazy workers

# Iterating over different step_sizes
for h in h_list:
    
    #initialising the variables
    Xh=0.5
    years = 500
    group_size=7
    a=0.2
    
    H_concentration = [] # Temporary List to store concentration value of hardworkers
    H_concentration.append(Xh)
    
    #iterating over different intervals
    for i in range(years*2):
        Xh_next = H_concentration[-1] + h*f(H_concentration[-1],group_size,a) # Estimation using euler scheme
        H_concentration.append(Xh_next)
    L_concentration = [1-x for x in H_concentration] #Temporary List to store concentration value of lazy workers
    H_overall_concentration.append(H_concentration)
    L_overall_concentration.append(L_concentration)

Visualisation.multi_visualisation(years,h_list,H_overall_concentration,L_overall_concentration,numerical=True)