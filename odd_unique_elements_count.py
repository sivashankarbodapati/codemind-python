def u(arr):
  ulst = []
  for x in arr:
    if x not in ulst:
       if x%2!=0:
          ulst.append(x)
  return ulst
t=int(input())
arr=list(map(int,input().split()))
res=u(arr)
print(len(res))