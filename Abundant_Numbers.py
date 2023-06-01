n = int(input())
s = 0
x = n
for i in range(1, n):
    if (n%i == 0) :
        s+=i
if s > x :
    print("True")
else :
    print("False")