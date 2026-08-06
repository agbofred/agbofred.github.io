def counters(problamSize):
    
    print(f"{'Problem size':<20} {'Iteration':>10}")
    print(f"{'------------':<20} {'---------':>10}")
    count =0
    currentSize = problamSize
    for i in range(5):
        
        while problamSize > 0:
            problamSize = problamSize // 2
            count += 1 
        print(f"{currentSize:<20} {count:>10}")
        currentSize  = currentSize ** 2
        problamSize = currentSize
    
counters(10)

problamSize = int(input("Enter the problem size: "))
print(f"{'Problem size':<20} {'Iteration':>10}")
print(f"{'------------':<20} {'---------':>10}")
count =0
currentSize = problamSize
while problamSize > 0:
    problamSize = problamSize // 2
    count += 1 
print(f"{currentSize:<20} {count:>10}")
currentSize  = currentSize ** 2
problamSize = currentSize