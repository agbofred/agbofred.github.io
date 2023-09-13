# Understanding Numeric 
A = 10
B = 5 % 3
C = A * B ** B
A -= B + A // 2
A, B, C = C, A, B
#print(A)

# Understanding Logical operation
A = 10
B = 4
C = "Quiz"
A *= B
if A > 40 and C != "C":
    B= 4
    # print(str(B)+C)
#else:
    #print(A < B or not (C == "C"))

# Defining a function
def even_days(n_days):
    count_days = 0
    for i in range(n_days):
        if i % 2 != 0:
            count_days += 1
    #return count_days
def divisible_by_six_or_seven(a,b):
    count =0
    while a <= b:
        if((a%6==0 or a%7==0) and not (a%6==0 and a%7==0)):
            print(a)
            count +=1
        a+=1
    return count

# Boilerplate code
if __name__ == '__main__':
    #total_even_days = even_days(31)
    counter = divisible_by_six_or_seven(40,60)
    print(counter)
