
# PYTHON LOOPS - COMPLETE NOTES
 
# Loop ka use same code ko multiple times run karne ke liye hota hai

# 1. FOR LOOP

# for loop tab use hota hai jab iterations ka number pata ho

print("FOR LOOP BASIC")

for i in range(5):   # range(5) -> 0 se 4 tak numbers deta hai
    print(i)

# Output
# 0 1 2 3 4

# RANGE FUNCTION

print("\nRANGE FUNCTION EXAMPLES")

# range(start, stop)

for i in range(1,6):  # 1 se 5 tak
    print(i)

# range(start, stop, step)

for i in range(1,10,2):   # step = 2
    print(i)

# LOOP THROUGH LIST

print("\nLOOP THROUGH LIST")

fruits = ["apple","banana","mango"]

for fruit in fruits:
    print(fruit)

# LOOP THROUGH STRING

print("\nLOOP THROUGH STRING")

for char in "Python":
    print(char)

# WHILE LOOP

# while loop tab use hota hai jab condition true rahe

print("\nWHILE LOOP")

i = 1

while i <= 5:
    print(i)
    i += 1   # increment zaruri hai warna infinite loop ban jayega

# INFINITE LOOP

# agar condition kabhi false na ho

print("\nINFINITE LOOP EXAMPLE (STOP MANUALLY)")

# while True:
#     print("Hello")

# BREAK STATEMENT

# break loop ko turant stop karta hai

print("\nBREAK EXAMPLE")

for i in range(10):
    if i == 5:
        break
    print(i)

# CONTINUE STATEMENT

# continue current iteration skip karta hai

print("\nCONTINUE EXAMPLE")

for i in range(5):
    if i == 2:
        continue
    print(i)

# ELSE WITH LOOP

# loop normally finish hone par else execute hota hai

print("\nLOOP ELSE")

for i in range(3):
    print(i)
else:
    print("Loop finished")

# NESTED LOOPS

# loop ke andar loop

print("\nNESTED LOOP")

for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)

# PRACTICE EXAMPLE

print("\nPRACTICE EXAMPLE")

# 1 se 10 tak even numbers print karo

for i in range(1,11):
    if i % 2 == 0:
        print(i)