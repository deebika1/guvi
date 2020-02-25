# program which is used to check the given string contanis vowel are not
def vowels1(string):
 len1=len(string)
 c=0
 for i in range(0,len1):
  if(string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u'):
   c=c+1
   #print(c)
   return c
# get the input string from the user
string=input()
result=vowels1(string)
if(result==1):
 print("yes")
else:
 print("no")


#Given a string S, print 'yes' if it has a vowel in it else print 'no'.
#Sample Testcase :
#INPUT
#codekata
#OUTPUT
#yes
