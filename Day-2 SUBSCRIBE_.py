# cook your dish here
def min_total_cost(T, test_cases):
    results = []
    for i in range(T):
        N, X = test_cases[i]
        # Calculate the number of subscriptions needed
        num_subscriptions = (N + 5) // 6  # This is equivalent to ceil(N / 6)
        # Calculate the total cost
        total_cost = num_subscriptions * X
        results.append(total_cost)
    return results

# Reading input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Getting the results
results = min_total_cost(T, test_cases)

# Printing results
for result in results:
    print(result)
