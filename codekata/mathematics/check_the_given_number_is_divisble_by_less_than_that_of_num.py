#Given a number N, check if N is divisible by any number less than N (ie.,it leaves no remainder)except 1.
num=int(input())
c=0
for i in range(2,num):
 if(num%i==0):
  c=1
if(c==1):
 print("yes")
else:
 print("no")
 
#Given a number N, check if N is divisible by any number less than N (ie.,it leaves no remainder)except 1.
#Input Size : 1 <= N <= 100000
#Sample Testcase :
#INPUT
#10
#OUTPUT
#yes
