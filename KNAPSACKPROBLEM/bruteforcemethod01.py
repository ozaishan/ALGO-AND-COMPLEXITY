def generate_binary_strings(n):
    
    return [bin(i)[2:].zfill(n) for i in range(2**n)]

def brute_force_01_knapsack(profits, weights, capacity):
   
    
    if len(profits) != len(weights):
        raise ValueError("Profits and weights lists must have the same length.")

    num_items = len(profits)
    max_profit = 0

    for binary_string in generate_binary_strings(num_items):
        total_weight = 0
        current_profit = 0

        for i in range(num_items):
            if binary_string[i] == '1':
                total_weight += weights[i]
                current_profit += profits[i]

        if total_weight <= capacity:
            max_profit = max(max_profit, current_profit)

    return max_profit

def brute_force_fractional_knapsack(profits, weights, capacity):
    
    if len(profits) != len(weights):
        raise ValueError("Profits and weights lists must have the same length.")

    num_items = len(profits)
    max_profit = 0

    for binary_string in generate_binary_strings(num_items):
        total_weight = 0
        current_profit = 0
        remaining_capacity = capacity

        for i in range(num_items):
            if binary_string[i] == '1':
                if weights[i] <= remaining_capacity:
                    current_profit += profits[i]
                    remaining_capacity -= weights[i]
                else:
                    fraction = remaining_capacity / weights[i]
                    current_profit += fraction * profits[i]
                    remaining_capacity = 0
                    break

        max_profit = max(max_profit, current_profit)

    return max_profit