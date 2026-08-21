############################################################
# Name:
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

def calc_months_to_savings(salary, savings_rate, des_amount=5000):
    """
    Function to calculate the number of months until a certain amount has
    been saved. Assumes savings starts at nothing and that the yearly interest
    rate is divided equally between months.
    """
    bank_interest_rate = 0.03
    current_savings = 0
    months = 0
    while current_savings < des_amount:
        months += 1
        current_savings += salary * savings_rate + current_savings * bank_interest_rate / 12
    return months


if __name__ == '__main__':
    SALARY = 1000
    RATE = 0.1
    print("Saving " + str(RATE) + " of $" + str(SALARY) +":")
    print("It will take", calc_months_to_savings(SALARY, RATE), "months to save $5000 or more.")

# put des_amount default parameter as second parameter on 7
# flip less than to greater than on 16
# move months increment to after 18
# flip salary and current_savings on 18
