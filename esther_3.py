# Problem D - Triangular Numbers
num = int(input())  # Do not change this line
triangle = 0
for i in range(1, num + 1):
    triangle += i
    print(triangle)