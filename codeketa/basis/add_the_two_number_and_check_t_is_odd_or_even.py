# find the sum of two number and sum is whether odd or even by using fucntion
def sum(num1,num2):
  sum1=num1+num2
  if(sum1%2==0):
    return 'even'
  else:
    return 'odd'
# get the two values from the user
num1,num2=list(map(int,input("").split()))
res=sum(num1,num2)
print(res)
