# program used to print Yes if N is between the range of N and R by using function
def range1(N,L,R):
 for i in range(L,R+1):
  if(i==N):
    c=1
    print("yes")
 return c
# get the value of N L R form the user
N=int(input())
L,R=list(map(int,input("").split()))
res=range1(N,L,R)
if(res==0):
 print("no")
