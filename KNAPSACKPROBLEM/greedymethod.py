def fractional_knapsack(profits, weights, capacity):

    if len(profits) != len(weights):
        raise ValueError("Profits and weights lists must have the same length.")
    
    ratios = [p / w for p, w in zip(profits, weights)]

    
    items = sorted(range(len(profits)), key=lambda i: ratios[i], reverse=True)

    total_weight = 0
    max_profit = 0

    for i in items:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            max_profit += profits[i]
        else:
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / weights[i]
            max_profit += profits[i] * fraction
            break

    return int(max_profit)