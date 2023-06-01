def revrs(num):
    rev = 0
    while num > 0 :
        rev = (rev*10) + num%10
        num//=10
    return rev

n = int(input())
n_sq = n*n # 144
n_rev = revrs(n) # 21
x = n_rev * n_rev
n_sq_rev = revrs(x) # 441

if n_sq == n_sq_rev :
    print("True")
else :
    print("False")