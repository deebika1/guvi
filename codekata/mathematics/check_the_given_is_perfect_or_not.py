# program whcih is used to check the given number is prefect or not
# prefect number means add ṭhe digit of the given number and should be the multiples of 3
def pure(num):
 s=0
 while(num>0):
   t=int(num%10)
   s+=t
   num=num//10
 return t
# get the value from the user
num=int(input())
# call the function and result should be stored in res
res=pure(num)
if(res%3==0):
 print("pure")
else:
 print("not")
