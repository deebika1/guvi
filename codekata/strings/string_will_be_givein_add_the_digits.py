# write the program which is used to sum the number persent in the given string
def carno(s):
 len1=len(s)
 sum1=0
 for i in range(0,len1):
  if(s[i].isdigit()):
   sum1=sum1+int(s[i])
 return sum1
# get the input string form the user
s=input()
result=carno(s)
print(result)



#In XYZ country there is rule that car’s engine no. depends upon car’ number plate. Engine no is sum of all the integers present on car’s Number plate.The issuing authority has hired you in order to provide engine no. to the cars.Your task is to develop an algorithm which takes input as in form of string(Number plate) and gives back
#Engine number.
#Input Description:
#You are given a string ’s’
#Output Description:
#Print the number plate
#Sample Input :
#HR05-AA-2669
#Sample Output :
#28
