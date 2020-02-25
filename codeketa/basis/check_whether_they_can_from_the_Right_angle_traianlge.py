# program which is used to find whether the given side can form the right angle triangle
def right_triangle(num1,num2,num3):
  if((num1*num1)+(num2*num2)==(num3*num3)):
    return "yes"
  else:
    return "no"
# get the nun1,num2,num3 value form the user
num1,num2,num3=list(map(int,input("").split()))
res=right_triangle(num1,num2,num3)
print(res)
    
