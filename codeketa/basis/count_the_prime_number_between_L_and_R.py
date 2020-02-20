# write the program which is used to count the prime number between the L and R
def prime(L,R):
# count is the variable which is used to count the number of prime number between the L and R range
 count=0
 for i in range(L,R+1):
   if(i>1):
    for j in range(2,i):
     if(i%j==0):
        break
    else:
      count=count+1
 return count
# get the value of L and R form the user
L,R=list(map(int,input("").split()))
res=prime(L,R)
print(res)
   
