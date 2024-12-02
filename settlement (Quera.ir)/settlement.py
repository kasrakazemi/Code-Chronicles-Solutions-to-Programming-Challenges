import numpy as np

# Function to find the person with max credit
def get_max_index(arr):
    return np.argmax(arr)

# Function to find the person with max debit
def get_min_index(arr):
    return np.argmin(arr)

# Minimize the cash flow among friends
def minimize_cash_flow(transactions):
    # Number of friends
    n = len(transactions)
    
    # Calculate the net amount each person owes/receives
    net_amount = [0] * n
    for i in range(n):
        for j in range(n):
            net_amount[i] += (transactions[j][i] - transactions[i][j])
    
    # Initialize the result matrix
    result = [[0] * n for _ in range(n)]
    
    # Recursive helper function to settle amounts
    def settle_amount(net_amount):
        # Find maximum creditor and maximum debtor
        max_credit = get_max_index(net_amount)
        max_debit = get_min_index(net_amount)
        
        # If no transactions left to settle, return
        if net_amount[max_credit] == 0 and net_amount[max_debit] == 0:
            return
        
        # Find minimum of amounts owed or receivable
        min_value = min(-net_amount[max_debit], net_amount[max_credit])
        net_amount[max_credit] -= min_value
        net_amount[max_debit] += min_value
        
        # Update the result matrix
        result[max_debit][max_credit] = min_value
        
        # Recursive call for the remaining unsettled amounts
        settle_amount(net_amount)
    
    # Call the helper function
    settle_amount(net_amount)
    
    # Return the final result matrix
    return result


transactions = [
   
]

for _ in range(3):
    li = input().split()
    transactions.append([int(x) for x in li])

# Get the minimized transaction matrix
result = minimize_cash_flow(transactions)

for row in result:
    print(" ".join(map(str, row)))
