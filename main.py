n = int(input())
x2 = []
for i in range(n):
    x = int(input())
    if x % 7 == 0:
        x2.append(x * x)
for i in x2:
    print(i)