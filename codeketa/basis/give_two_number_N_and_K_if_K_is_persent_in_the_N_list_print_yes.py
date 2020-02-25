# program which is used to print yes if K is persent in the list
def function1(N,K):
 l=list(map(int,input("").strip().split()))[:N]
 for i in range(0,N):
  count=0
  if(K==l[i]):
   count=count+1
   return count
# get the value of N and K form the user
N,K=list(map(int,input("").split()))
res=function1(N,K)
if(res==1):
 print("yes")
else:
 print("no")
