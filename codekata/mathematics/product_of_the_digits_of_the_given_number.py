# program which is used to calculate the product of the digits of the given number by using function
# the digit function is used to separate the digit for the given number and product the digits
def digit(num):
 f=1
 while(num>0):
  t=int(num%10)
  f=f*t
  num=num//10
 return f
# get the number form the user
num=int(input())
# call the function and the result is stored in res
res=digit(num)
print(res)

 


              

  
 
