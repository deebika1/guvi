# program whcih is used to remove the space and used to calculate the lenght of the string by using function
def length(str):
# remove the space betweent the string
 remove=str.replace(" ","")
 # calculate the length of the stirng
 length1=len(remove)
 return length1
# get the string from the user
str=input("")
# call the function and store the result in res
res=length(str)
print(res)
