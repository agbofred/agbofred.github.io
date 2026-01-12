# Write your code below:

def main():
    m1 = Matrix(3, 3, 2)
    m2 = Matrix(3, 3, 4)
    print(m1 + m2)
    m1 = Matrix(4, 4, 2)
    m2 = Matrix(4, 4, 4)
    print(m2 - m1)
    m1 = Matrix(2, 3, 2)
    m2 = Matrix(3, 2, 4)
    print(m1 * m2)

if __name__ == "__main__": main()