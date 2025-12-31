def calculate_bounce_height(current_height):
    bounce_height = current_height * 0.80
    return bounce_height

def is_ball_stopped(height):
   if height < 1 :
       return True
   else:
       return False 

def simulate_bouncing_ball(start_height):
    bounce_count = 0 
    
    total_distance = start_height
    current_height = start_height

    while not is_ball_stopped(current_height):
        current_height = calculate_bounce_height(current_height)
        bounce_count += 1 

        if not is_ball_stopped(current_height) :
            total_distance += 2 * current_height

    return bounce_count, total_distance

    


# Test your code heres
print("Testing Bouncing Ball Simulation...")
