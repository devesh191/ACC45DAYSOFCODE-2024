# cook your dish here
def water_filling_time(test_cases):
    results = []
    for B1, B2, B3 in test_cases:
        # Count the number of empty bottles (where Bi = 0)
        empty_count = (1 - B1) + (1 - B2) + (1 - B3)
        
        if empty_count >= 2:
            results.append("Water filling time")
        else:
            results.append("Not now")
    
    return results

# Read input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = water_filling_time(test_cases)

# Output results
for result in results:
    print(result)
