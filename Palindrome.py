n = int(input())
x = n
rev = 0
while n > 0 :
    rev = (rev*10) + (n%10)
    n//=10
    
if rev == x :
    print("True")
else :
    print("False")