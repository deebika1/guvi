# count the number of digits for the given number by using function
def count(num):
 c=0
 while(num>0):
   c=c+1
   num=num//10
 return c
# get the num form the user
num=int(input())
# call the function and the result is stored in res
res=count(num)
# print the result
print(res)
