# find the area of an equilateral triangle by using function
import math
def area(a):
 res=(math.sqrt(3)/4)*(a*a)
 res1=round(res,2)
 return res1
# get the area value from the user
a=float(input())
res2=area(a)
print(res2)
