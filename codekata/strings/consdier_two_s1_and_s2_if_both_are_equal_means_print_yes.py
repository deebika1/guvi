s1,s2=list(map(str,input().split()))
len1=len(s1)
len2=len(s2)
c=0
if(len1==len2):
  for i in range(0,len1):
    if(s1[i]==s2[i]):
      c=c+1
if(c==len1):
  print("yes")
else:
  print("no")
      
#Given 2 strings S1 and s2, check whether they are case senitively equal without using any predefined function(case sensitive).If they are not same print 'no'
#Sample Testcase :
#INPUT
#guvi guvi
#OUTPUT
#yes
