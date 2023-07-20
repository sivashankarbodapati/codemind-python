l,r,k = map(int,input().split())
c = 0
for x in range(l,r+1):
   if(x%k == 0):
     c+=1
print(c)