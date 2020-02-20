# program which is used to print yes if their product is perfect square or else print no
def square1(N,M):
 prod=N*M
 c=N**2
 if(prod==c):
  print("yes")
 else:
  print("no")
# get the value of N and M form the user
N,M=list(map(int,input("").split()))
square1(N,M)
