# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    round_trip = (one_way_km * 2 ) / km_per_liter * price_per_liter
    if round_trip <= budget:
        return True 
    else:
        return False
print("Testing Road Trip Budgeter...")
