/*Given a number N followed by N numbers. Keep the count of each number and print the maximum repeating number.
Input Size : N <= 100000
Sample Testcase :
INPUT
5
15 5 -20 -20 -45
OUTPUT
-20
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
max1=max(arr)
# print(max1)
ind=arr.index(max1)
# print(ind)
print(l[ind])
