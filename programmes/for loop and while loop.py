def sum(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    return total_sum
num = 1234578
print("Sum of digits using while loop:", sum(num))

def sum(num):
    total_sum = 0
    for i in str(num):
        total_sum += int(i)
    return total_sum
num = 12345
print("Sum of digits using for loop:", sum(num))
