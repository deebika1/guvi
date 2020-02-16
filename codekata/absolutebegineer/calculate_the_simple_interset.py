# program which is used to calculate the simple interset by using function
def simple(P,N,R):
 SI=(P*N*R)/100
 interset=round(SI,2)
 return interset
# get the value of P N R from the user
P,N,R=list(map(float,input("").split()))
res=simple(P,N,R)
print(res)
