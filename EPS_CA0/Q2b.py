import matplotlib.pyplot as plt
import numpy as np
np.random.seed(515)
import random
def determineVote(p):
    return 1 if random.random() < p else 0
def determineOnesAndZeros(personNums,p):
    zeros=0
    ones=0
    for i in range(personNums):
        result=determineVote(p)
        if(result==0):
            zeros+=1
        else:
            ones+=1
    return [ones,zeros]
p=0
results=0
counter=0
finals=list()
while p<=1:   
    results=0
    counter=0
    for i in range(1000):
        onesAndZeros=determineOnesAndZeros(12,p)
        if onesAndZeros[0]>onesAndZeros[1]:
            counter+=1
    results=counter/1000
    finals.append(results)
    p+=0.1
import matplotlib.pyplot as plt
indexes = [i * 0.1 for i in range(len(finals))]
plt.plot(indexes, finals, marker='o')
plt.xlabel('Probabilities')
plt.ylabel('Acuracy')
plt.grid(True)
plt.show()