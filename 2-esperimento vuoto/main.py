import numpy as np
from IPython import embed
import matplotlib.pyplot as plt
from datetime import datetime

def andamento(array):
    
    end_index = 0
    result = []

    soglia = 0.09

    # fino a che ci sono elementi nella lista
    while end_index < len(array)-1:

        # se l'elemento start è minore di end [CRESCENTE]
        if (array[end_index])+soglia < array[end_index+1]:

            # fino a che l'elemento con endindex+1 è maggiore di endindex
            result.append(1)

        # se l'elemento start è maggiore di end [DECRESCENTE]
        elif (array[end_index])-soglia > array[end_index+1]:

            # fino a che l'elemento con endindex+1 è minore di endindex            
            result.append(-1)

        # se l'elemento start è uguale a end [STABILE]
        else:
            
            # fino a che l'elemento con endindex+1 è uguale a endindex
            result.append(0)

        end_index += 1

    return result

# Read the data from the file, skipping the first part (e.g., first 108 lines)
data = np.genfromtxt('report.asc', delimiter='\t', skip_header=155, dtype=None, encoding='utf-8', names=True)

time = []
T_Shroud = []
T_Cold = []
P_Full_range = []
P_Chamber = []
T_Setpoint = []


#tiro fuori i dati dal file caricato in precede
for row in data:
    time.append(datetime.strptime(row[0], "%d/%m/%y %H:%M:%S"))
    T_Shroud.append(row[1])
    T_Cold.append(row[2])
    P_Full_range.append(row[17])
    P_Chamber.append(row[19])
    T_Setpoint.append(row[30])
   

# print(time[0])
# print(T_Shroud[0])
# print(T_Cold[0])
# print(P_Full_range[0])
# print(P_Chamber[0])
# print(T_Setpoint[0])



fig, axs = plt.subplots(2, 2)

fig.set_figheight(15)
fig.set_figwidth(15)


axs[0,0].plot(time, T_Shroud,  color="red")
axs[0,0].set_title("T_Shroud")
axs[1,0].plot(time[:-1], andamento(T_Shroud), color="blue", linestyle="dotted")
axs[1,0].set_title("Andamento 1: crescente  0: Stabile -1: Decrescente")
axs[1,0].set_yscale("linear")

#t shroud e t setpoint vs date_time
axs[0,1].set_title("T_Shroud e T_setpoint Vs Date_Time")
axs[0,1].plot(time, T_Shroud, color="red", label="T_Shroud")
axs[0,1].plot(time, T_Setpoint, color="blue", label="T_Setpoint")
axs[0,1].legend()

#P Full Range 1 chamber-ITR90 e P Chamber Vs Date_time
axs[1,1].plot(time,P_Full_range, color="Green")
axs[1,1].plot(time,P_Chamber, color="Purple")
axs[1,1].set_yscale("log")

plt.tight_layout(pad=3.0)
plt.show()
