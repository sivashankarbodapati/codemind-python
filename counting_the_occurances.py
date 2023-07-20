s = input()
lst =[]
for i in s:
  lst.append(i)
ans = lst.count(input())
if ans == 0:
    print("-1")
else:
  print(ans)