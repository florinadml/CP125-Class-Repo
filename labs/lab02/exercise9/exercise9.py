# Lab 02 Exercise 9: Level Up Calculator
# Write your code below:

def calculate_xp_required(current_level):
   xp_required = current_level * 100
   return xp_required

def can_level_up(xp_remaining, xp_required):
    if xp_remaining >= xp_required :
        return True 
    else:
        return False
    
def simulate_leveling(total_xp):
    current_level = 1 
    xp_remaining = total_xp
    xp_required = calculate_xp_required(current_level)
    while can_level_up(xp_remaining, xp_required):
        xp_required = calculate_xp_required(current_level)
        xp_remaining += calculate_xp_required(current_level)
        current-level += 1 

    return current_level, xp_remaining

# Test your code here
print("Testing Level Up Calculator...")
