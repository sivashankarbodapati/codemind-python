def Prime(n):
    if (n <= 1) :
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else :
        return True
    
a = int(input())
b = int(input())
c = 0
for i in range(a, b+1):
    if Prime(i):
        c+=1
print(c)