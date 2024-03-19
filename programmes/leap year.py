# year= int (input("enter year:"))
# if (year % 400 == 0) and (year % 100 == 0):
#  print("{0} is a leapyear".format(year))
# elif(year%4==0) and (year%100!=0):
#   print("{0} is a leap year.".format(year))
# else:
#   print("{0} is not a leap year.".format(year))
  
y=int(input("y"))
if (y%400 == 0) and(y %100 ==0):
    print ("{0} i l y".format(y))
elif (y%4==0) and (y%100!=0):
       print ("{0} i l y.".format(y))
else:
    print("{0} is n l y .".format(y))