/*Given 2 numbers N and K and followed by an array of N integers. The given element K is removed from the array and new array is printed. If after removing every occurance of K the array becomes empty, print 'empty' without quotes.
Example:
Input: {10,10,20,30,76}, K=10
Output: {20,20,76}
Input Size : N <= 100000
Sample Testcase :
INPUT
5 10
10 10 20 30 76
OUTPUT
20 30 76*/
n,k=list(map(int,input().split()))
l=input().split(" ")
a=[]
# print(n,k);
# print(l)
for val in l:
    # print(val)
    if int(k) != int(val):
        a.append(val)
if(a!=[]):
 print(" ".join(a))
else:
 print("empty")
