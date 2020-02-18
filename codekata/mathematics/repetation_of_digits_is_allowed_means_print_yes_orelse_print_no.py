# program whcih is used find the repetation of digits if it means print yes or not
def repetation(num):
 while(num>0):
  t=num%10
  all.append(t)
  num=num//10
#print(all)
 return all
# check1 function is used to check if any repetation of digits is persent or not
def check1(res1):
 len1=len(all)
 res=len1-1
#print(res)
 for i in range(0,res+1):
  for j in range(i+1,res+1):
   if(all[i]==all[j]):
    return "yes"
 else:
    return "no"
# get the num value form the user
num=int(input())
all=[]
res1=repetation(num)
res2=check1(res1)
print(res2)


 
