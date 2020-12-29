/* Given a number N followed by N numbers. Find the largest number which can be formed from the given numbers and print it.
NOTE: Each number should be used exactly once.
Input Size : 1 <= N <= 100000
Sample Testcases :
INPUT
5
5 6 7 8 9
OUTPUT
98765 
*/
n=int(input())
l1=[int(i) for i in input().split()][:n]
result=list(sorted(l1,reverse=True))
# print(result)
s=''
for i in result:
    # print(i)
    s+=str(i)+''
print(s)
