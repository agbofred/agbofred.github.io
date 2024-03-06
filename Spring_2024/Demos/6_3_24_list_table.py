import random

score=[]
for i in range(30):
    score.append(random.randint(50,100))

#score =[random.randint(50,100) for i in range(30)] # with comprehension
count=[0]*5
for i in range(len(score)):
    if score[i]>=90:
        count[0] +=1
    elif score[i]>=80:
        count[1]+=1
    elif score[i]>=70:
        count[2]+=1
    elif score[i]>=60:
        count[3]+=1
    else:
        count[4]+=1
L=["A","B","C","D","F"]
for i in range(len(count)):
    print(f'{L[i]} --> {count[i]}')
print(score)