def atm(): # This is the atm function
    balance =1000
    end =False
    while not end:
        choice =input("\nEnter 1 to check balance; 2 to withdraw; 3 to deposit; and 0 to exit ")
        if choice =="":
            return "Invalid operation"
        else:
            if int(choice)==1:
                print("Your balance is ", balance)
            elif int(choice)==2 and balance>0:
                amount= int(input("Enter the amount to withdraw "))
                if amount<=balance:
                    print("withdrawal of ", amount, " was successful ")
                    balance -=amount
                else:
                    print("Sorry! You do not have enough balance to withdraw ", amount)
            elif int(choice)==3:
                    depamount= int(input("Enter the amount to deposit "))
                    balance +=depamount
                    print("Your deposit of ", amount, " was successful and your balance is", balance)
            elif int(choice)==0:
                return
            else:
                end = True
        
def count_character():
    sentence = input("\nPlease make a sentence: ")
    sentence_no_space = sentence.replace(" ","")

    print("Number of words without spaces: ",len(sentence_no_space))
    print("\nNumber of words in sentence: ",len(sentence))

# Grade calculator problem

def test(weight):
    score = int(input("\n Enter the test score: "))
    return score * weight
def homework(weight):
    score = int(input("\n Enter the homework score: "))
    return score * weight
def project(weight):
    score = int(input("\n Enter the project score: "))
    return score * weight
def compute_grade():
    t= test(0.2)
    h = homework(0.2)
    p = project(0.3)
    weighted_score =t+h+p
    percent_weighted = (weighted_score*100)/70
    print("\n============= Results analysis==========\n")
    print("Your assignment weighted score is ", round(weighted_score), 'out of', 70)
    if percent_weighted <= 50:
        print("\nWARNNING!!! You have scored below average in your assignments. " )
        print("You must work harder in your finals to obtain a passing grade!!!:" )
    elif percent_weighted < 70:
        print("\nYour cummulative grade is ", round(percent_weighted),'% => D.', "You would need an estimated ", 70 - weighted_score + (100 * 0.3), " points to clinch an A grade" )
    elif percent_weighted < 80:
       print(" ")
       print("Your cummulative grade is ", round(percent_weighted),'% => C.', "You would need an estimated ", 70 - weighted_score + (100 * 0.3), " points to clinch an A grade" )
    elif percent_weighted < 90:
        print(" ")
        print("Your cummulative grade is ", round(percent_weighted),'% => B.', "You would need an estimated ", 70 - weighted_score + (100 * 0.3), " points to clinch an A grade" )
    else:
        print(" ")
        print("You're in a good academic standing and would need only about ", 70 - weighted_score + (100 * 0.3), " points to retain an A grade" )
        

    
    




if __name__=="__main__":
    #atm()
    #count_character()
    compute_grade()