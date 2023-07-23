import matplotlib.pyplot as plt

#Simple visualisation
def visualisation(years,H_concentration,L_concentration):
    semesters=[i+1 for i in range(years*2)]
    plt.plot(semesters, H_concentration, label = "hard-working Concentration")
    plt.plot(semesters, L_concentration, label = "Lazy-working Concentration")
    plt.xlabel("Semester")
    plt.ylabel("Concentration")
    plt.legend()
    plt.show()


 # Function for Visualisation
def multi_visualisation(years,group_size_list,H_concentration,L_concentration,numerical):
    # Visualisation of Xh
    semesters=[i+1 for i in range(years*2)]
    for i in range(len(H_concentration)):
        if i%10!=0:
            if numerical==False:
                plt.plot(semesters, H_concentration[i],color='gray',linestyle='dashed')
            else:
                plt.plot(semesters, H_concentration[i][:-1],color='gray',linestyle='dashed',label = str(group_size_list[i]))
        else:
            if numerical==False:
                plt.plot(semesters, H_concentration[i],label = str(group_size_list[i]))
            else:
                plt.plot(semesters, H_concentration[i][:-1],label = str(group_size_list[i]))
    
    plt.xlabel("Semester")
    plt.ylabel("Concentration")
    plt.legend(title='group_size')
    plt.show()

    # Visualisation of Xl
    semesters=[i+1 for i in range(years*2)]
    for i in range(len(H_concentration)):
        if i%10!=0:
            if numerical==False:
                plt.plot(semesters, L_concentration[i],color='gray',linestyle='dashed')
            else:
                plt.plot(semesters, L_concentration[i][:-1],color='gray',linestyle='dashed',label = str(group_size_list[i]))
        else:
            if numerical==False:
                plt.plot(semesters, L_concentration[i],label = str(group_size_list[i]))
            else:
                plt.plot(semesters, L_concentration[i][:-1],label = str(group_size_list[i]))
    plt.xlabel("Semester")
    plt.ylabel("Concentration")
    plt.legend(title='group_size')
    plt.show()

