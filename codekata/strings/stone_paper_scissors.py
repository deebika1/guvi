# program whcih is used to print which won the match
def stone_paper_scissors(a,b):
  if(a=='R' and b=='P'):
    return 'P'
  elif(a=='R' and b=='S'):
    return 'R'
  elif(a=='S' and b=='P'):
    return 'S'
  else:
    return 'D'
# get the string form the user
a,b=input("").split()
res=stone_paper_scissors(a,b)
print(res)
