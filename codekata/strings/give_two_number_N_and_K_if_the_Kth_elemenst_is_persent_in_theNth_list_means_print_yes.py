#Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.
n,k=list(map(int,input().split()))
l=[int(i) for i in input().split()][:n]
c=0
for i in l:
  if(i==k):
    c=1
if(c==1):
  print("yes")
else:
  print("no")

#Given 2 numbers N,K and an array of N integers, find if the element K exists in the array.
#Input Size : N <= 100000
#Sample Testcase :
#INPUT
#5 2
#1 2 3 4 5
#OUTPUT
#yes
#HINT: Read about Binary Search
