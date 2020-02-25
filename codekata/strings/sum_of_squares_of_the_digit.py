#Given a number N, print the sum of the squares of its digits.
#INPUT
#19
#OUTPUT
#82
n=int(input())
sum=0
while(n>0):
  t=n%10
  sum=sum+t**2
  n=int(n//10)
print(sum)
