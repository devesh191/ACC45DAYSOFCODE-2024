# cook your dish here
# Read number of test cases
T = int(input())

# Initialize a list to store results
results = []

# Process each test case
for _ in range(T):
    N = int(input())  # Read the weight of the pulp in kgs
    notebooks = 10 * N  # Calculate the number of notebooks
    results.append(notebooks)  # Store the result

# Output the results
for result in results:
    print(result)
