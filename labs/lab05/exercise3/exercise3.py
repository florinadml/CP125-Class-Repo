
def find_bottleneck_index(traceroute):
    max_jump = 0 
    bottle_neck_index = 0

    for i in range ( len(traceroute)- 1):
        current_latency = traceroute[i][1]
        next_latency = traceroute[i+1][1]

        jump = abs(next_latency - current_latency)

        if jump > max_jump : 
            max_jump = jump 
            bottle_neck_index = i
             
    return bottle_neck_index
      

# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
