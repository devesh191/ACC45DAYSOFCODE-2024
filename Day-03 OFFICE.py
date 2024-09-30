# cook your dish here
# Number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read X and Y
    X, Y = map(int, input().split())
    
    # Calculate total working hours in the week
    total_hours = (4 * X) + Y
    
    # Print the result
    print(total_hours)
