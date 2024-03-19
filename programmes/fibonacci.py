# def fibonacci(n):
#   a, b = 0, 1
#   for i in range(n):
#     a, b = b, a+b
#   return a

#   for i in range(10):
#    print(fibonacci(i))
num=int(input("enter any no:"))
n1,n2 = 0,1
sum=0


for i in range (0,num):
    print (sum,end=" ")
    n1=n2
    n2=sum
    sum=n1+n2
# def fibonacci(n):
#   a, b = 0, 1
#   for i in range(n):
#     a, b = b, a+b
#   return a

# # Generate the first ten numbers in the Fibonacci series
# for i in range(19):
#   print(fibonacci(i),  end = " " )



