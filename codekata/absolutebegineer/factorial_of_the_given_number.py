# find the factorial of the given number
def factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
# get the number form the user
num=int(input())
res=factorial(num)
print(res)

  
  
