#pip install tabulate
import os
from tabulate import tabulate

equipos = [["team1",12],["team2",15],["team3",2]]

for i in range(len(equipos)):
    for j in range(i+1):
        if(equipos[i][1] > equipos[j][1]):
            aux = equipos[i]
            equipos[i] = equipos[j]
            equipos[j] = aux
        
    
print(tabulate(equipos,headers=["NOMBRE","PJ"]))