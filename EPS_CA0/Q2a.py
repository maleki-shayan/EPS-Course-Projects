from math import comb
def calculate_majority_probability(zeros,ones,p):
    majority=None
    minority=None
    if(zeros<ones):
        majority=ones
        minority=zeros
    else:
        majority=zeros
        minority=ones   
    soorat = 0.5*(p ** majority) * ((1 - p) ** minority)
    makhraj = 0.5*(p ** majority) * ((1 - p) ** minority) + 0.5*(p ** minority) * ((1 - p) ** majority)
    probability=soorat/makhraj
    return probability
print(calculate_majority_probability(4,8,0.7))
print(calculate_majority_probability(2,10,0.7))
print(calculate_majority_probability(4,8,0.3))
print(calculate_majority_probability(3,9,0.5))
print(calculate_majority_probability(7,5,0.5))