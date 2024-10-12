# cook your dish here
def min_bags_needed(T, test_cases):
    results = []
    for i in range(T):
        N, K, M = test_cases[i]
        capacity_per_bag = K * M
        bags_needed = (N + capacity_per_bag - 1) // capacity_per_bag
        results.append(bags_needed)
    return results

T = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = min_bags_needed(T, test_cases)

for result in results:
    print(result)