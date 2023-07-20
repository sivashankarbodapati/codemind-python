def Fact(n):
    fact = 1
    for i in range(1,n+1):
      fact*=i
    return fact
    
t = int(input())
for i in range(t):
  item = int(input())
  ans = Fact(item)
  print(ans)