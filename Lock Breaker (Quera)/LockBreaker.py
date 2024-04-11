import collections

# Define a function to cycle characters in a string
def cycle(s, n):
    d = collections.deque(s)
    d.rotate(n)
    return "".join(d)

# Define a function for big integer addition
def big_add(num1, num2):
    answer = ""
    carry = 0 
    
    while (num1 != "") or (num2 != "") or (carry != 0):
        if (num1 != "") and (num2 != ""):
            temp = int(num1[-1]) + int(num2[-1]) + carry
        if (num1 == "") and (num2 == ""):
            temp = carry
        if (num1 == "") and (num2 != ""):
            if carry == 0:
                answer = num2 + answer
                break
            temp = int(num2[-1]) + carry
        if (num1 != "") and (num2 == ""):
            if carry == 0:
                answer = num1 + answer
                break
            temp = int(num1[-1]) + carry
        
        answer = str(temp % 10) + answer
        carry = int(temp / 10)
        num1 = num1[:-1]
        num2 = num2[:-1]
    
    return answer

# Input two numbers as strings
number1 = input()
number2 = input()

# Remove spaces from input numbers
number1 = number1.replace(" ", "")
number2 = number2.replace(" ", "")

SumResult = 1

# Iterate through rotations of number1
for i in range(len(number1) + 1):
    number1Rotated = cycle(number1, -i)
    
    # Iterate through rotations of number2
    for j in range(len(number2) + 1):
        number2Rotated = cycle(number2, j)
        
        # Calculate the sum of the first three digits from the rotated numbers
        Sum = big_add(number1Rotated[1:4], number2Rotated[1:4])[1:]
        SumResult = int(Sum)
        
        # Check if the sum is divisible by 6
        if int(Sum) % 6 == 0:
            print('Boro joloo :)')
            break
    
    # If the sum is not divisible by 6, print "Gir oftadi :("
    if SumResult % 6 != 0:
        print('Gir oftadi :(')
    
    break  # Exit the loop after the first iteration
