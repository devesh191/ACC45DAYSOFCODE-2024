# cook your dish here
# Function to determine if there is a monopoly in the market
def check_monopoly(test_cases):
    results = []
    
    for profits in test_cases:
        P, Q, R, S = profits
        
        # Calculate the sum of profits of the other companies
        sum_other_A = Q + R + S
        sum_other_B = P + R + S
        sum_other_C = P + Q + S
        sum_other_D = P + Q + R
        
        # Check for monopoly condition
        if P > sum_other_A or Q > sum_other_B or R > sum_other_C or S > sum_other_D:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read number of test cases
T = int(input())
test_cases = []

# Read all test cases
for _ in range(T):
    profits = list(map(int, input().split()))
    test_cases.append(profits)

# Get results for each test case
results = check_monopoly(test_cases)

# Print all results
for result in results:
    print(result)
