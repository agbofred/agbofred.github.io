# stud_record ={
#     "100": 20,
#     "101": 50,
#     "102": 70
# }
# for key in stud_record:
#     print(f"{key} -----> {stud_record[key]}")
    
def read_dic(filename):
    dic ={}
    with open(filename) as fh:
        for line in fh:
            key, value = line.strip().split(":")
            dic[key]=value
    return dic

def check_score(): # Checking grades for each students 
    score = read_dic("dic_file.txt")
    finnished = False
    while not finnished:
        get_id=input("Enter a student's ID: ")
        if get_id=="":
            finnished=True
        else:
            if get_id in score:
                print(f"The student with ID {get_id} scored {score[get_id]}")
            else:
                print(f"No student with ID {get_id} was found in the record")

def students_with_scores():
    score =read_dic("dic_file.txt")
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
students_with_scores()               
#check_score()
    