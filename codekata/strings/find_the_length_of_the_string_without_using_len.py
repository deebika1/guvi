# the program which is used to print the length of the string without using the len function
def without_lib(string):
 count=0
 for i in string:
   count=count+1
 return count
# get the input string from the user
string=input()
result=without_lib(string)
print(result)


#Given a string S, find its length without using any pre-defined functions.
#Sample Testcase :
#INPUT
#codekata
#OUTPUT
#8
