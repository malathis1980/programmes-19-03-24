num = int(input("Please Enter any Number: "))
Sum = 0
while(num > 0):
    Reminder = num % 10
    Sum = Sum + Reminder
    num = num//10

print("\n Sum of the digits of Given Number = %d" %Sum)

num = int(input("Enter any Number = "))
tot = 0

for i in range(len(str(num))):
    tot += num % 10
    num //= 10

print("Sum of the digits of Given Number  = ", tot) 
