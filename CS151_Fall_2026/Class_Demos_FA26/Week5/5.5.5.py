def members_birthday():
    """
    Here is the birthday program
    Enter your name: Joe
    Enter your birth month: April
    Enter your birth year: 1985
    """
    col1Label = "Name"
    col2Label = "Birth Month"
    col3Label = "Age"
    table = f"{col1Label:<10s} {col2Label:<15s} {col3Label:<5s}"
    birthdays = ""
    for i in range(2):
        name = input("Enter your name: ")
        month = input("Enter your birth month: ")
        year = int(input("Enter your birth year "))
        birthdays += f"{name:<10s} {month:<15s} {2026 - year:<5d}" + "\n"
    print("-"*30)
    print(table)
    print("-"*30)
    print(birthdays)

members_birthday()