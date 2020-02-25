#Given a number N, print the sum of its first and last digit.
num=int(input())
all=[]
while(num>0):
 t=num%10
 all.append(t)
 num=int(num//10)
len1=len(all)
sum=all[0]+all[len1-1]
print(sum)

#Given a number N, print the sum of its first and last digit.
#Input Size : |N| <= 10000
#Sample Testcase :
#INPUT
#51233
#OUTPUT
#8
