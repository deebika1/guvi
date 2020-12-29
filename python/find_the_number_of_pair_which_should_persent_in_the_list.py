/*Given a limit N followed by N numbers, find the number of pairs such ai + aj = ak for all i < j < k.
Input Size : 3 <= N <= 1000
Sample Testcase :
INPUT
5
1 4 2 3 5
OUTPUT
3
*/
n=int(input())
l=[int(i) for i in input().split()][:n]
# print(n,"\n",l)
arr=[]
for i in range(0,len(l)):
    sum1=0
    m=l[i]
    for j in range(0,len(l)):
        if(i!=j):
         sum1=sum1+m+l[j]
         arr.append(sum1)
# print(arr)
mylist = list(dict.fromkeys(arr))
# print(mylist)
count=0
for i in mylist:
    for j in l:
        if(i==j):
            # print(i,j)
            count=count+1
print(count)
        
        
        
