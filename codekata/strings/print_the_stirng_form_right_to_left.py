# program which is used to get the reverse the string in the reversed string first letter should be upper
def reverse(string):
 rev=string[-1::-1]
 print(rev[0].upper()+rev[1:])
# get the input string from the user
string=input()
reverse(string)


#Jennyfer is fond of strings. She wants to read the character from right to left, so she wants you to design a suitable algorithm which satisfy her desire.

#Input Description:
#Enter the string ‘s’
#Output Description:
#Print the string from characters right to left.
#Sample Input :
#jennyfer
#Sample Output :
#Refynnej
