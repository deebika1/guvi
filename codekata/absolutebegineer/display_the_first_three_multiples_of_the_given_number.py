# program which is used to print the first three multiples of the given number
def mul(num):
 for i in range(1,4):
   res=num*i
   print(res,' ',end='')
# get the value form the user
num=int(input())
mul(num)
