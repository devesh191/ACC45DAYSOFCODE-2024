# cook your dish here
T=int(input())
for i in range(T):
    a,b,c,d=map(int,input().split())
    A=max(a,b)
    B=max(c,d)
    print(A+B)