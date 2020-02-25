#Given a sentence and string S, find how many times S occurs in the given sentence.If S is not found in the sentence print -
n=input()
s=input()
count=0
res1=n.split()
#print(res1)
for i in range(0,len(res1)):
 if(res1[i]==s):
   count=count+1
   break
if(count==0):
 print("-1")
else:
 print(count)
 
 
#Given a sentence and string S, find how many times S occurs in the given sentence.If S is not found in the sentence print -1
#Input Size : |sentence| <= 1000000(complexity O(n)).
#Sample Testcase :
#INPUT
#I enjoy doing codekata
#codekata
#OUTPUT
#1
