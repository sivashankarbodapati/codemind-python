string = input()
c=0
for char in string:
  if char.isdigit():
      c+=1
if c == 0:
    print("Doesn't contain digit")
else:
  print(f"Contains {c} digit")