/*Given 2 numbers N and K followed by N numbers such that sum of two pairs in the N numbers results K value, if it exist print 'yes' otherwise 'no'.
Input Size : N<=100000
Example:
INPUT
4 4
1 2 2 4
OUTPUT
yes*/
n,k=list(map(int,input().split()))
l=[int (i) for i in input().split()][:n];
# print(n,k,l)
p=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        c= int(l[i])+int(l[j])
        if(c==int(k)):
            p=1;
            break;
if(p==0):
    print("no")
else:
    print("yes")
