/* You are given with list of numbers,Your task is to find the maximum count of the numbers which are consecutively increasing in list

Input Description:
You are given a number n denoting size of array,Next line contains ‘n’ space separated numbers.

Output Description:
Print the desired result

Sample Input :
6
1 2 0 3 4 5
Sample Output :
4*/
n=int(input())
l=list(map(int,input().split(" ")))
# print(n,l)
count=1
r=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] <l[j]:
            count=count+1;
        else:
         count=1
    r.append(str(count))
    break;
print(" ".join(r))
            
    
