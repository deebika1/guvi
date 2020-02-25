n,k=list(map(str,input().split()))
d=int(k)
for i in range(d-1,len(n)+1,d):
  c=n[i]
  print(c,end='')
  if(i<len(n)-1):
    print(end=' ')
 #Given a string and a number K.Print every kth character from the beginning.
#Sample Testcase :
#INPUT
#string 3
#OUTPUT
#r g
