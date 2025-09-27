"""i=1
print("even numbers are\n:")
while i < 6:
 if(i%2==0):
  print("even",i)
 else:
  print("odd",i)
 i+=1




i=1
while i < 6:
 i += 1
 
 if(i==3):
  continue
 print(i)
 
fruits = ("apple", "banana", "cherry")
for x in fruits:
  print(x)
print(type(x))"""


print("multiplication of table is:\n ")

for x in range(1,11):
 for y in range(1,11):
  print(f"{x:2}*{y:2}={x*y:2}",end=" ")
 print()
