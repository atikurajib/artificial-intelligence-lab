# Objective Function
function OBJECTIVE-FUNCTION(state):
    total_value = 0
    for each buyer-seller match in state:
        value = buyer_satisfaction + seller_profit
        total_value += value
    return total_value

# Cost Function
function COST-FUNCTION(state):
    total_cost = 0
    for each buyer-seller match in state:
        cost = transaction_cost + delivery_cost
        total_cost += cost
    return total_cost

# Hill Climbing Algorithm (using both)
function HILL-CLIMB(problem):
    current = initial state of problem
    repeat:
        neighbor = highest valued neighbor of current
        if (OBJECTIVE-FUNCTION(neighbor) - COST-FUNCTION(neighbor)) <= 
           (OBJECTIVE-FUNCTION(current) - COST-FUNCTION(current)):
            return current
        current = neighbor
