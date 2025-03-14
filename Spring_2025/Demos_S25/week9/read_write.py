from filechooser import choose_input_file, choose_output_file

filename = choose_input_file()
try:
    with open(filename, "w") as fh:
        
        #print(fh.read())
        #print(fh.readlines())
        #print(fh.read().splitlines()) # The same as using fh as iterator
        data =[]
        for i in fh:
            data.append(i.strip())# to remove the \n from the list, use .strip()
        print(data)

except IOError:
    print("File does not exist")
    
    
################### CLASS REVIEW ###############
# A=[[i+j for i in range(3)] for j in range(4)]
# print([A[i][2] for i in range(len(A))])

A=[]
for j in range(4):
    a=[]
    for i in range(3):
        a.append(i+j)  
    A.append(a)
        
print(A)
        