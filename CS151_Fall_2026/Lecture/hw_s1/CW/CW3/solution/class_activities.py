""" 
Task: Create a program that:
Starts with a balance of 1000
Shows menu options (check balance, withdraw, deposit)
Updates balance after transactions
Prevents overdraft (balance < 0)
Continues until user chooses to exit
"""
def atm():
    bal =1000
    ending = False
    while not ending:
        choice = input("Enter: 1 to Check Balance; 2 to Withdraw; 3 to Deposit; 0 to Exit : ")
        if int(choice)== 1:
            print("Your current balance is ", bal)
        elif int(choice)== 2 and bal>=0:
            amount = int(input("How much do you want to withdraw?  "))
            if amount <= bal:
                print("Withdrawal of ", amount, "successful!")
                bal -=amount
            else:
                 print("Sorry! You do not have sufficient balance to withdraw ", amount)
        elif int(choice)== 3:
            deposit =int(input("Enter the amount you want to deposit: "))
            bal +=deposit
            print("Your current balance is  ", bal)
        elif int(choice)== 0:
            return 
        else:
            choice =""
            ending = True


# Problem 2
"""
Program that counts the number of strings and 
"""
def word_count():
    # Word and Character Counter Program

    # Get input from user
    sentence = input("Please enter a sentence: ")

    # Count total characters (excluding spaces)
    char_count = len(sentence.replace(" ", ""))

    # Count total words
    #words = sentence.split()
    word_c = len(sentence)

    # Count vowels (optional feature)
   
    # Display statistics
    print("\n=== Text Statistics ===")
    print(f"Total characters (excluding spaces): {char_count}")
    print(f"Total words: {word_c}")

#Problem 3
"""Grade Calculator"""

def get_test(weight): # get the score and its weight
    score = float(input("Enter the test score: "))
    return score * weight

def get_homework(weight): # get the homework and its weight
    score = float(input("Enter the homework score: "))
    return score * weight

def get_project(weight): # get the project and its weight
    score = float(input("Enter the project score: "))
    return score * weight


def compute_grade():
    test = get_test(0.2)
    homework = get_homework(0.2)
    project = get_project(0.3)

    weighted_score = test + homework + project

    print(" ")
    print("============== Result Summary ======================= ")
    print(" ")
    print("Your assignment weighted score is ", round(weighted_score), '/', 70)
    percent_weighted = (weighted_score*100)/70
   
    if percent_weighted <= 50:
        print(" ")
        print("WARNNING!!! You have scored below average in your assignments. " )
        print("You must work harder in your finals to obtain a passing grade!!!:" )
    elif percent_weighted < 70:
        print(" ")
        print("Your cummulative grade is ", round(percent_weighted),'% => D.', "You would need an estimated ", 70 - weighted_score + (100 * 0.3), " points to clinch an A grade" )
    elif percent_weighted < 80:
       print(" ")
       print("Your cummulative grade is ", round(percent_weighted),'% => C.', "You would need an estimated ", 70 - weighted_score + (100 * 0.3), " points to clinch an A grade" )
    elif percent_weighted < 90:
        print(" ")
        print("Your cummulative grade is ", round(percent_weighted),'% => B.', "You would need an estimated ", 70 - weighted_score + (100 * 0.3), " points to clinch an A grade" )
    else:
        print(" ")
        print("You're in a good academic standing and would need only about ", 70 - weighted_score + (100 * 0.3), " points to retain an A grade" )
        

if __name__ =='__main__':
    compute_grade()