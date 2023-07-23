## 4TH Order Kutta Method
import School
import Visualisation


# Defining f(x) which is the slope
def f(Xh):
    return Xh*(1-Xh)*(1/group_size-a)


# # Initialising the variables
Xh=0.5
group_size=7
a=0.2
years = 500
H_concentration = [] # List to store concentration value of hardworkers
H_concentration.append(Xh)

h = 1
# Iterating over time intervals
for i in range(years*2):
    K1 =  h * f(H_concentration[-1])
    K2 = h * f(H_concentration[-1] + 0.5*K1)
    K3 = h * f(H_concentration[-1] + 0.5*K2)
    K4 = h * f(H_concentration[-1] + K3)

    Xh_next = H_concentration[-1] + ((1/6) * (K1+ (2*K2) +(2*K3) +K4 )) # Estimating next value using 4th RK method
    H_concentration.append(Xh_next)

L_concentration = [1-x for x in H_concentration] # List to store concentration value of lazy workers

Visualisation.visualisation(years,H_concentration[:-1],L_concentration[:-1])    #Visualising the concentration over the years
