num = input("Enter numbers: ").split() # eneter the no by space
 
largest = 0
second_largest = 0
 
for i in num:
 
    i = int(i)
 
    if i > largest:
        second_largest = largest # (20 =10)
        largest = i      #(20 =20)
 
print(largest)
print(second_largest)
