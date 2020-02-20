# program to print the sum of first n natural number by using function
def natural(num):
 if(num<=100000): 
# s is the variable that is intially 0 to store the sum of all naturall number
  s=0
  for i in range(1,num+1):
   s+=i
  return s
# get the num value form the user
num=int(input())
res=natural(num)
# to display the sum of n natural number is
print(res)
