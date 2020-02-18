# the program whcih is used to find the greatest number that greatest number should be divide the both num1 and num2
# the max function is used to get the greatest number among the two number
def max(num1,num2):
 if(num1>num2):
   return num1
 else:
  return num2
# check1 function is used to check the greatest number is divisible for both the num1 and num2
def check1(res1,num1,num2):
 if(res1%num1==0 and res1%num1==0):
   return num1
 else:
   return num2
# get the num1 and num2 value from the user
num1,num2=list(map(int,input("").split()))
res1=max(num1,num2)
res2=check1(res1,num1,num2)
print(res2)

