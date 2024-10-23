# cook your dish here
# cook your dish here
import math
for i in range(int(input())):
    h,x,y=map(int,input().split())
    if x>=y:
        print(math.ceil(h/x))
    else:
        print(math.ceil((h-y)/x)+1)