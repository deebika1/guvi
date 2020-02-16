# program which is used to find the smallest number among two number by using function
def small(num1,num2):
 if(num1<num2):
  return num1
 else:
  return num2
# get the value num1 and num2 form the user
# the syntax to get the value in single line
num1,num2=list(map(int,input("").split()))
# call the function and the result is stored in res
res=small(num1,num2)
print(res)
