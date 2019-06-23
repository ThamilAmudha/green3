s = input()
t = ["a","e","i","o","u","A","E","I","O","U"]
c=len(s)
for i in range(0,c):
  if(s[i] in t):
    print("yes")
    break
else:
  print("no")
