# Accept the number of steps 
steps_input = input("Enter the number of steps taken each day in the month, separated by spaces: ")

# Convert the input string to a list of integers
steps = list(map(int, steps_input.split()))

# Calculate the highest and lowest step 
highest_steps = max(steps)
lowest_steps = min(steps)

# Calculate the average daily step 
average_steps = sum(steps) / len(steps)

# Sort the step counts in descending order
sorted_steps = sorted(steps, reverse=True)

# Display the results
print(f"Highest step count: {highest_steps}")
print(f"Lowest step count: {lowest_steps}")
print(f"Average daily step count: {average_steps:.2f}")
print(f"Step counts in descending order: {sorted_steps}")