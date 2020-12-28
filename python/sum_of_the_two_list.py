/*Given a number N followed by 2 lists A and B of N integers each. Form a 3rd list C of size N where each element of list C is the sum the respective elements in lists A and B.
Input Size : N <= 100000
Sample Testcase :
INPUT
5
30 5 5 30 -45
1 2 3 4 5
OUTPUT
31 7 8 34 -40

*/
n=int(input())
l1=[int(i)for i in input().split()][:n]
l2=[int(i) for i in input().split()][:n]
# print(n,"\n",l1,"\n",l2)
s=[]
for i in range(0,len(l1)):
    sum=0;
    for j in range(0,len(l2)):
      if(i==j):
          sum+=l1[i]+l2[j]
        #   print(sum)
          break
          
    s.append(str(sum))
print(" ".join(s))
