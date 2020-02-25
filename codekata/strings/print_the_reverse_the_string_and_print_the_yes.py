#Given a string S, print 'yes' if it is a palindrome or 'no' if it is not a palindrome.
def palindrome(string):
 rev=string[-1::-1]
 if(string==rev):
  return "yes"
 else:
  return "no"
# get the string from the user
string=input()
result=palindrome(string)
print(result)

#Given a string S, print 'yes' if it is a palindrome or 'no' if it is not a palindrome.
#Sample Testcase :
#INPUT
#lappal
#OUTPUT
#yes
