no=int(input("enter no="))
print ("factors of no {} are :".format(no))
for i in range (1,no+1):
    if (no%i==0):
        print(i)
        