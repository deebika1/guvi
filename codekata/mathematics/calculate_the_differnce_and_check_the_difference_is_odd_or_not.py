# program is used to find the difference between the given two number and the difference is even or odd
def difference(num1,num2):
 sub=num1-num2
 return sub
# get the value of num1 and num2 form the user
num1,num2=list(map(int,input("").split()))
# call the function and the result is stored in res
res=difference(num1,num2)
if(res==0 or res%2==0):
  print("even")
else:
 print("odd")
 
