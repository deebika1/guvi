# program used to print Yes if N is between the range of N and R by using function
def range1(N,L,R):
 c=0
 for i in range(L,R+1):
  if(i==N):
   c=c+1
   return c
# get the value of N L R form the user
N=int(input())
L,R=list(map(int,input("").split()))
res=range1(N,L,R)
if(res==1):
 print("yes")
else:
 print("no")
