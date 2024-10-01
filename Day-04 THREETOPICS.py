# cook your dish here
# Read the input
input_data = input().strip()
A, B, C, X = map(int, input_data.split())

# Check if X is one of the topics A, B, or C
if X in (A, B, C):
    print("Yes")
else:
    print("No")
