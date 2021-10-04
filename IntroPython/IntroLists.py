# https://dropbox.com/work/CMP464788Fall2021_DataHandlingAndAnalysis


def lists():
    #  Lists (Similar to Java)
    values = [1, 3, 5, 7, 9]
    print(values)  # Prints values
    print(values[0])  # Prints value at index
    print(values[-1])  # Prints value at last index
    print(values[-2])  # Prints value at second to last index

    #  List slicing (Creating new lists from existing lists)
    print(values[0:3])  # Extracts the first 3 values
    print(values[:3])  # '  '
    print(values[1:4])  # Extracts starting at index 1 and ending at 3
    print(values[1:-1])  # Extracts list starting at index 1 and excluding last index

    #  List can contain different data types
    list_one = [1, 0.142, True, "Wednesday", [1, 2, 3]]

    #  Useful methods
    #  Length of lists
    print(len(list_one))

    #  Append a value to list
    list_one.append(4)
    print(list_one)

    #  Extract and remove the last value of a list
    val = list_one.pop()
    print(val)
    print(list_one)

    #  Find the index of a value
    ind = list_one.index("Wednesday")
    print(ind)

    #  Looping through lists
    names = ['Alice', 'Bob', 'Charles']
    for name in names:
        print(name)

    #  Looping with index
    for idx, name in enumerate(names):
        print(str(idx) + " " + name)

    #  List comprehension: Transform list without a for loop
    scores = [60, 70, 80, 90, 85]
    new_scores = []
    for score in scores:
        new_score = score + 5  # Add 5 to each score from original list
        new_scores.append(new_score)
    print(new_scores)

    # Alternative single statement comprehension
    new_student_scores = [score + 5 for score in scores]  # Expression + where the values come from and where to
    # append
    print(new_student_scores)

    # Increase scores by 10%
    curved_scores = [score * 1.1 for score in scores]
    print(curved_scores)

    # Double the size of values in list
    ary_one = [1, 3, 5, 7, 11]
    ary_two = [nums * 2 for nums in ary_one]
    print(ary_two)


def sets():
    # Create a set
    set_one = {1, 2, 3}
    print(set_one)

    # Convert between lists and sets
    list_two = [1, 2, 3, 4]
    set_two = set(list_two)
    print(set_two)

    list_three = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8]
    set_three = set(list_three)
    print(set_three)
    list_three_updated = list(set_three)
    print(list_three_updated)


def tuples():
    # Tuples - immutable, values are still accessible
    tuple_one = (1, 2, 3)
    list_four = [1, 2, 3]
    list_four[0] = 100
    print(list_four)
    # tuple_one[0] = 100 - Does not work, Tuples can not be modified
    print(tuple_one)


def dictionary():
    # Dictionaries
    score_dict = {
        "Alice": 85,
        "Bob": 87,
        "Clare": 88
    }
    print(score_dict["Alice"])  # Extract values from dictionary
    print("David" in score_dict)  # Check if an item is in dictionary
