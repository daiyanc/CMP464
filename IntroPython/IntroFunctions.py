# https://dropbox.com/work/CMP464788Fall2021_DataHandlingAndAnalysis


def get_sum(list_one):
    """
    Returns the sum of list_one
    :return: sum
    """
    sum_val = 0
    for val in list_one:
        sum_val += val
    return sum_val


def get_sum_and_average(values):  # A Python function can return more than one item
    """
    Returns sum and average of a list
    :param values:
    :return: sum and avg
    """
    sum_val = get_sum(values)
    avg = sum_val / len(values)
    return sum_val, avg


list2 = [1, 2, 3]
list_sum, list_avg = get_sum_and_average(list2)
print(get_sum(list2))
print(list_sum, list_avg)

