def Digits(s):
  if any(char.isdigit()for char in s):
     print("Yes")
  else:
     print("No")
t = int(input())
for i in range(t):
  string = input()
  Digits(string)