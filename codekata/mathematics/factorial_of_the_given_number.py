# program whcih is used to find the factorial of the given nunber
def factorial1(num):
    s=1
    for i in range(1,num+1):
        s=s*i
    return s
#get the value form the user
num=int(input(""))
res=factorial1(num)
print(res)
