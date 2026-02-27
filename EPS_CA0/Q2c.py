from Q2a import calculate_majority_probability
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
while p<=1:   
    results=0
    counter=0
    for i in range(1000):
        onesAndZeros=determineOnesAndZeros(12,p)
        if onesAndZeros[0]>onesAndZeros[1]:
            counter+=1
    results=counter/1000
    p+=0.01
    if(results==1):
        print(p)
        break
