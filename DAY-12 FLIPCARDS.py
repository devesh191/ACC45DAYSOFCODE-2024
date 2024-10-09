# cook your dish here
# cook your dish here
t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    if n!=x:
        print(min(x,n-x))
    else:
        print("0")