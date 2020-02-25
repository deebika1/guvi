# You are given a ‘true’ string. String is called true if weight of string is multiple of 8. Your task is to tell whether a string can be declared True or Not. 
#Weight of string is the sum of ASCII value of Vowel character(s) present in the string.
def ascii_value(string):
 sum=0
 len1=len(string)
 for i in range(0,len1):
  if(string[i]=='a'):
    sum=sum+97
  elif(string[i]=='e'):
    sum=sum+101
  elif(string[i]=='i'):
    sum=sum+105
  elif(string[i]=='o'):
    sum=sum+111
  elif(string[i]=='u'):
    sum=sum+117
 return sum
# check function is used to find the sum which is multiple of 8
def check(res):
 c=0
 if(res%8==0):
  c=c+1
 return c
# get the string form the user
string=input()
res=ascii_value(string)
result=check(res)
print(result)


#You are given a ‘true’ string. String is called true if weight of string is multiple of 8. Your task is to tell whether a string can be declared True or Not. Weight of string is the sum of ASCII value of Vowel character(s) present in the string.
#Input Description:
#You are given as string ‘s’ in lower cases
#Output Description:
#Print 1 for true and 0 for false
#Sample Input :
#raja
#Sample Output :
#0
