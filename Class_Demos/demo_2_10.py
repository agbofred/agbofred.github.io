def f(x,y=0):
    z = (x + 3) ** 2
    return y + z

x1 = 2
y1 = 1
z = x1 + f(y1,x1)
#print(z)

def make_change(cost, amount_paid):
    # List of available bill denominations
    denominations = [20, 10, 5, 2, 1]

    # Initialize a dictionary to store the count of each denomination
    change_dict = {}

    # Calculate the change to be given
    change = amount_paid - cost

    # Iterate through the denominations and calculate the count of each denomination
    for denom in denominations:
        count = change // denom
        if count > 0:
            change_dict[denom] = count
            change -= count * denom

    # Print the results
    #print("Change to be given:")
    #for denom, count in change_dict.items():
       # print(f"${denom}: {count} bills")

# Example usage
make_change(22, 40)  # Change for $21 with $50 paid

def give_change(price, paidamt):
    balance = paidamt - price
    
    if(balance//20 >0) and (balance%20>10):
        change = balance//20
        print(f'$20 - {change:>5}')
    balance = change*20
    if(balance//10 >0) and (balance%10<=balance):
        change = balance//10
        print(f'$10 - {change:>5}')
    balance = change*10
    if(balance//5 >0) and (balance%5<=balance):
        change = balance//5
        print(f'$5 - {change:>5}')
    balance = change*5
    if(balance//2 >0) and (balance%2<=balance):
        change = balance//2
        print(f'$2 - {change:>5}')
    balance = change*2
    if(balance//1 >0) and (balance%1<=balance):
        change = balance//1
        print(f'$1 - {change:>5}')
    balance = change*1

def checkchange(a):
    count =0
    if a>20:
        count +=1
         

give_change(20,40)