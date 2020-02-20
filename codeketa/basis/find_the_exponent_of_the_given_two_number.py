# program which is used to calculate the exponent of the given number
def no(num1,num2):
 c=(num1**num2)
 return c
# get the value of num1 and num2 from the user
num1,num2=list(map(int,input("").split()))
res1=no(num1,num2)
# print the result of the exponential of the two number
print(res1)
