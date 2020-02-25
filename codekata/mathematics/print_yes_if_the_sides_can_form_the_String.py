# program which is used to print yes with the given sides we can form the trianlge orelse print no
def triangle(num1,num2,num3):
# to check along with the given side we can form the triangle
# the sum of length of any two sides is greater than the third side means print no
  if(num1+num2<=num3) or (num2+num3<=num1) or (num1+num3<=num2):
   return "no"
  else:
   return "yes"
# get the num1 num2 and num3 value form the user
num1,num2,num3=map(int,input().split())
# call the triangle function and the result is stored in res
res=triangle(num1,num2,num3)
# to print the result
print(res)

#Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.
#Input Size : A,B,C <= 100000
#Sample Testcase :
#INPUT
#3 4 5
#OUTPUT
#yes
