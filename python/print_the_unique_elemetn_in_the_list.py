/*Given a number N followed by an array of N integers, every element appears twice except for one. Find that single one and print it.
Input Size : N <= 100000
Sample Testcase :
INPUT
5
30 5 5 30 -45
OUTPUT
-45
*/
n=int(input())
l=[int(i) for i in input().split()][:n]
# print(n,"\n",l);
arr=[]
for i in range(0,len(l)):
    count=0;
    for j in range(0,len(l)):
        if int(l[i])==int(l[j]):
            count=count+1
    arr.append(count)
# print(arr)
max1=min(arr)
# print(max1)
ind=arr.index(max1)
# print(ind)
print(l[ind])
