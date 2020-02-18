# program whcih is used to check the value of N is power of K
def power1(N,K):
 if(N==K*K):
  return "yes"
 else:
  return "no"
# get the value of N and K form the user
N,K=list(map(int,input("").split()))
res=power1(N,K)
print(res)
