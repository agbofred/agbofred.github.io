def add():
    sum = 0
    stop = False
    while not stop:
        num= int(input("Enter a number: "))
        if num == 0:
            stop = True
        elif(num%2==0):
            print("This is not an even number")
        else:
            sum += num
    return(sum)

#print(add())

for i in range(20,1,-1):
    print(i)

