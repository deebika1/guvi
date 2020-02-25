# program which is used to reverse the word of the string
def reverse1(str):
# slpit the words of string separated by space
 str=str[-1::-1]
# now join words with space
 output=' '.join(str)
 return output
# get the string form the user
str=input().split()
res=reverse1(str)
print(res)
 
