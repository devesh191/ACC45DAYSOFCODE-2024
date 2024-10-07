# cook your dish here
# cook your dish here
for _ in range(int(input())):
    W,X,Y,Z= map(int,input().split())
    if W==X or W==Y or W==Z or W==X+Y or W==Y+Z or W==Z+X or W==X+Y+Z:
        print("YES")
    else:
        print("NO")
    