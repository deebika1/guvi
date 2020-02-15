# program which is used to find the length of the circumference
def circumference(num):
 if(num>=0):
  leng=(2*(22/7)*num)
  leng1=round(leng,2)
  return leng1
 else:
  print("Error")
# get the length form the user
num=float(input())
res=circumference(num)
print(res)
