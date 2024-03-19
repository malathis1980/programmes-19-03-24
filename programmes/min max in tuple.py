def min_max_tuple(input_tuple):
    if not input_tuple:
        return None
    else:
        return min(input_tuple), max(input_tuple)


numbers = (5, 3, 8, 2, 10)
min_num, max_num = min_max_tuple(numbers)
print("Minimum number:", min_num)
print("Maximum number:", max_num)