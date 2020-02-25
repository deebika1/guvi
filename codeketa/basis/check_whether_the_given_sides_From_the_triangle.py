# program whcih is used to print yes if the triangle is scalene
def scalene(num1,num2,num3):
 if(num1!=num2 and num1!=num3 and num2!=num3):
  return "yes"
 else:
  return "no"
# get the num1 num2 and num3 form the user
num1,num2,num3=list(map(int,input("").split()))
res=scalene(num1,num2,num3)
print(res)
# scalene triangle is formed when the all the three sides are not equal
