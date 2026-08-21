import random 

score=[]
[score.append(random.randint(50, 100)) for i in range(20)]
score_count = [0]*5
for i in range(len(score)):
    if score[i]>=90:
        score_count[0]+=1
    elif score[i]>=80:
        score_count[1] +=1
    elif score[i]>=70:
        score_count[2] +=1
    elif score[i]>=60:
        score_count[3] +=1
    else:
        score_count[4] +=1
        
leter_grade =["A", "B", "C", "D", "F"]
for i in range(len(score_count)):
    print(f"{leter_grade[i]}----->{score_count[i]}")

print(score_count)
print(score)

Li=[3,4,5]
l2 =["r",5]

magic = [ [2, 9, 4], [7, 5, 3], [6, 1, 8] ]
print(magic[-2][-2])
