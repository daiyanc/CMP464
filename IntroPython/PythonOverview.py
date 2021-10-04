# https://dropbox.com/work/CMP464788Fall2021_DataHandlingAndAnalysis


def intro():
    # If-Else Branches
    age = 23
    drinking_age = 21
    if age >= drinking_age:
        print("You are old enough to buy liquor.")
    else:
        print("You are not old enough to buy liquor.")
    print("End.")

    # For Loops
    for letter in ['B', 'A', 'C', 'D', 'E']:
        print(letter)
    print(letter)

    for num in range(5, 12):
        print(num)

    # Multiple loop index
    for num, j in zip((range(10)), range(10, 20)):
        print("i:", num, end=", ")
        print("j:", j)

    # Loop with step
    for num in range(0, 10, 2):  # last argument determines step size
        print(num)

    # First 100 Integers
    total = 0
    for num in range(1, 101):
        total += num
    print(total)

    print(sum(range(1, 101)))  # Using sum function
