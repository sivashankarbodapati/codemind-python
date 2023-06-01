s = 0
t = int(input())
vals = input()
lst = vals.split()
for i in lst:
    if (int(i)%2 == 0):
        s = s + int(i)
print(s)