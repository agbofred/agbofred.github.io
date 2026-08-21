# build a table os scores as shown below
""" 
A -> 4
B -> 3
C -> 2
.
:
F -> 1
"""

import random 

score = []
#for i in range(20):
    #score.append(random.randint(50,100))

#  version 
[score.append(random.randint(50,100)) for i in range(20)]

score_count =[0]*5
for i in range(len(score)):
    if(score[i]>=90):
        score_count[0] +=1
    elif(score[i]>=80):
        score_count[1] +=1
    elif(score[i]>=70):
        score_count[2] +=1
    elif(score[i]>=60):
        score_count[3] +=1
    else:
        score_count[4] +=1
        
Leter_grade =["A", "B", "C", "D", "F"]
for i in range(len(score_count)):
    pass
    #print(f"{Leter_grade[i]} -> {score_count[i]}")
#print(score)
str = """
    This is Friday
    and it is a sunny
    day 
    """
#print(str.strip().splitlines())

l1=["44,",34,5]
l2=["This is", "making", "the news"]

print("-".join(l2))