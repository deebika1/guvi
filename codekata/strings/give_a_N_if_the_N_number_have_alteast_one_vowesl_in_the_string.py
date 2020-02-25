#Given a number N and an array of N strings,Print yes, if all strings have atleast one vowel in them otherwise print no.
num=int(input())
c=0
for i in range(0,num):
 a=input()
for i in range(0,num):
 if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
  c=1
if(c==1):
 print("yes")
else:
 print("no")
#Given a number N and an array of N strings,Print yes, if all strings have atleast one vowel in them otherwise print no.
#Input Size : N <= 1000
#sample Testcase :
#INPUT
#5
#code
#overload
#vishal
#sundar
#anish
#OUTPUT
#yes
