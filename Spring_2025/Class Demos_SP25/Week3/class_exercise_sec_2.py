def atm():
    balance = 1000
    finished = False
    while not finished:
        choice = input("\n Enter 1 to check balance; 2 to withdraw; 3 to deposit, and 0 to exit ")
        if choice=="":
            print("\n Invalid operation ")
            finished = True
        else:
            if int(choice) == 1:
                print("\n Your balance is ", balance)
            elif int(choice)== 2 and balance >=0:
                amount = int(input("\n Type the amount to withdraw: "))
                if amount <= balance:
                    print("\n Withdrawal of",amount,  "was successful ")
                    balance-=amount
                else:
                    print("\n Sorry! You do not have enough balance to withdraw ",amount)
            elif int(choice) == 3:
                dep = int(input("\n How much are you depositing? "))
                balance +=dep
                print("\n Your deposit was successful ")
            elif int(choice) == 0:
                finished = True
                return
            else:
                return
# Count character 

def count_character():
    seq = input("\nPlease type your sentences ....: ")
    seq_no_space= seq.replace(" ","")
    print("\n Sequence without space is ", len(seq_no_space))
    print("\n sequence with spaces ",len(seq))


def test(weight):
    test_score = float(input("\n Enter the test score: "))
    return test_score * weight
def homework(weight):
    homework_score = float(input("\n Enter the homework score: "))
    return homework_score * weight
def project(weight):
    project_score = float(input("\n Enter the project score: "))
    return project_score * weight

def compute_grade ():
    test_score = test(0.2)
    homework_score = homework(0.2)
    project_score = project(0.3)

    weighted_score = test_score+ homework_score + project_score

    print("\n============== Result Summary ======================= \n")
    print("Your assignment weighted average is ", round(weighted_score), 'out of', 70)




if __name__ =="__main__":
    #atm()
    #count_character()
    compute_grade()
