# pint the smallest number among the two number
def small(num1,num2):
 if(num1>num2):
   return num2
 else:
   return num1
# get the two numbers form the user
num1,num2=int(input())
res=small(num1,num2)
print(res,end="")
