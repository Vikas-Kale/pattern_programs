# Write a program to print number triangle pattern.
#
rows=5
for i in range(rows+1):
    for j in range(i):
        print(i,end=" ")
    print()


# Inverted pyramid of numbers.
rows=5
b=0
for i in range(rows,0,-1):
    b=b+1
    for j in range(1,i+1):
        print(b,end=" ")
    print("\r")
