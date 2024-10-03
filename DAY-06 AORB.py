# cook your dish here
def max_score(T, cases):
    results = []
    for X, Y in cases:
        # Calculate scores for A first then B
        score_A_first = max(500 - 2 * X, 0) + max(1000 - 4 * (X + Y), 0)
        # Calculate scores for B first then A
        score_B_first = max(1000 - 4 * Y, 0) + max(500 - 2 * (X + Y), 0)
        # Store the maximum of both scores
        results.append(max(score_A_first, score_B_first))
    return results

# Input handling
T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]
results = max_score(T, cases)

# Output the results
for result in results:
    print(result)
