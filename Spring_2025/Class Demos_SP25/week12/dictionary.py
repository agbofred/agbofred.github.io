# A = {True: 'Seth', False: 'Jesse', (1,3,5): "LIST"}
# if 10 in A:
#     print(A[10])
# else:
#     print("Key does not exit")

# score ={
#     "100": 70,
#     "200": 80,
#     "102": 100
# }
    
# for key in A:
#     print(f"{key}--------> {A[key]}")

def read_grade(filename):
    dic={}
    with open(filename) as fh:
        for line in fh:
            key, value = line.strip().split(":")
            dic[key]=value
    return dic
def check_score():
    score = read_grade("dic_text.txt")
    finnished = False
    while not finnished:
        get_id= input("Input your student ID ")
        if get_id=="":
            finnished = True
        else:
            if get_id in score:
                print(f"The students with ID {get_id} scored {score[get_id]}")
            else:
                 print(f"The students with ID {get_id} does not exist")
                 
#check_score()
def students_with_scores():
    score =read_grade("dic_text.txt")
    done= False
    while not done:
        what_score =input("insert the score in integer:  ")
        if what_score=="":
            done =True
        else:
            for st_id, value in score.items():
                if int(value)==int(what_score.strip()):
                    print(f"The student with ID {st_id} scored {value}")
                #else:
                    #print(f"No student with score {value} was found")
#students_with_scores()  

a={"i": "Fred"}
print(a.get("8","Nothing"))