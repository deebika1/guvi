# check whether the given number is odd or even by using function
def fun(num):
 num1=round(num)
 if(num!=0):
  if(num1%2==0):
    print("Even")
  else:
   print("Odd")
 else:
  print("Zero")
 
# get the value form the user
num=float(input())
# call the function
fun(num)
