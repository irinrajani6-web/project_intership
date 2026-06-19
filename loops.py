
print("while loop")
i=0
while i<10:
    print(i)
    i+=1

print("for loop")
for j in range(10):
    print(j)    
    
print(" break contiune and passs staement")
k = 1
while k < 6:
  print(k)
  if k == 3:
    break
  k += 1

for l in range(1, 6):
    if l == 3:
        continue
    print(l)

for m in range(6):
    if m == 3:
        pass
    print(m)