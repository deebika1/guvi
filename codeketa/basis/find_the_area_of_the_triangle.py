# program which used to find the area of the traingle if length and breadth are given by using function
def triangle1(B,H):
# area which is used to calculate the area of the triangle
  area=(B*H)/2
  return area
# get the value of base and height form the user
B,H=list(map(int,input("").split()))
res1=triangle1(B,H)
print(res1)
