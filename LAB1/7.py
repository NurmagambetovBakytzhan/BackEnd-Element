x = int(input())
y = int(input())

x2 = int(input())
y2 = int(input())

if(x == x2 and y != y2 or x != x2 and y == y2):
    print("YES")
else:
    print("NO")