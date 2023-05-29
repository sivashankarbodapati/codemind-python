def Sum(n) :
    s = 0
    while n > 0 :
        rem = n%10
        s = s+rem
        n//=10
    if (s > 9) :
        Sum(s)
    else :
        print(s)

num = int(input())
Sum(num)