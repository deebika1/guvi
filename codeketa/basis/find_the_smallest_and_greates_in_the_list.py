# program which is used to find the min and maximum index position of the element
n=int(input())
# a is the list which is used to split the element upto n
a=list(map(int,input().strip().split()))[:n]
# index which is used to find the minimum number index position
m=a.index(min(a))
# index which is used to find the maximum number index position
k=a.index(max(a))
print(m+1,k+1)
