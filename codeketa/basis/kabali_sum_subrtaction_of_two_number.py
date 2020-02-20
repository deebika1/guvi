# program to find the difference between two parties 
def parties(num1,num2):
# condition said that num1 should never greater than num2
  if(num2>num1):
# to find the difference between the num1 and num2
    diff=num2-num1
  return diff
# get the num1 and num2 value form the user
num1,num2=list(map(int,input("").split()))
res=parties(num1,num2)
print(res)
