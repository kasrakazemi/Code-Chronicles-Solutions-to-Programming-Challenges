# water columns height
height = [5, 2, 1, 3, 1, 4]
# total trapped water in the beginning
total_water = 0

# Loop through each column from the second column to the second-to-last column.
for column in range(1, len(height) - 1):
    # Find the maximum height to the left of the current column.
    max_left = max(height[0:column])

    # Find the maximum height to the right of the current column.
    max_right = max(height[column + 1:])

    # Calculate the effective height of the current column (minimum of max_left and max_right).
    eff_height = min(max_left, max_right)

    # Calculate the amount of water that can be trapped in the current column.
    water_column = eff_height - height[column]

    # Ensure water_column is greater than 0 before adding to total_water.
    if water_column > 0:
        total_water += water_column

# Print the total amount of trapped water.
print("Total trapped water:", total_water)
