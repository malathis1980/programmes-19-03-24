def is-prime(no):
if no==0 or no==1:
    print("the no {0} is prime")
else: 
    for i in range (2,no):

def is_prime(number):
    if number == 0 or number == 1:
        print(f"The number {number} is NOT the prime number.")
    elif number == 2:
        print(f"The number {number} is the prime number.")
    else:
        for i in range(2, number):
            if number % i == 0:
                check = "is NOT"
                break
            else:
                check = "is"
        print(f"The number {number} {check} the prime number.")