# check the given string is palindrome or not if it is a palindrome print 1 or print 0
def palindrome(string):
 rev=''.join(reversed(string))
#print(rev)
 if(rev==string):
   return "1"
 else:
  return "0"
# get the input string from the user
string=input()
result=palindrome(string)
print(result)


#Radha newly learnt about palindromic strings.A palindromic string is a string which is same when read from left to right and also from right to left.Help her in implementing the logic.
#input Description:
#You are given a String ‘s’
#Output Description:
#Print 1 if String is palindrome or 0 if not
#Sample Input :
#NITIN
#Sample Output :
#1
