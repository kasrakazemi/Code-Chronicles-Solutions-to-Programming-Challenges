# Define the wheel and password
whell = "RTIGFIPR"
password = "GFI"

# Function to find all occurrences of a character in the wheel
def find_letters(character):
    output_list = []
    for index, item in enumerate(whell):
        if character == item:
            output_list.append([index, item])

    return output_list

# Function to find the shortest distance from the pointer to a character
def find_distance(pointer, letters):
    minimums = []

    for i in letters:
        start_point = pointer
        end_point = i[0]
        clockwise = (end_point-start_point) % len(whell)
        anti_clockwise = (start_point-end_point) % len(whell)
        minimums.append([i[0], min(clockwise, anti_clockwise)])

    output_list = min(minimums, key=lambda x: x[1])

    return output_list[0], output_list[1]

pointer = 0  # Initial pointer position
total_rotations = 0  # Total rotations needed to reach the characters
total_time = 0  # Total time taken to reach the characters

# Iterate through each character in the password
for i in (password):
    letters = find_letters(i)
    pointer, rotations = find_distance(pointer, letters)
    total_rotations += rotations
    total_time += 1

# Print the total duration (time + rotations) to reach all password characters
print('Total Duration: ', total_time + total_rotations, 's')
