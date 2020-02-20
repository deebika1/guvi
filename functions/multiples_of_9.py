# write the program to print the multiple of nine upto the given number
def loop(num):
 for i in range(1,num+1):
  res=9*i
  print(res,end='')
  if(i<num):
    print(end=' ')
# get the number form the user
num=int(input())
loop(num)
