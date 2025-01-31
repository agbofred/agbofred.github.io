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
    


if __name__ =='__main__':
    atm()