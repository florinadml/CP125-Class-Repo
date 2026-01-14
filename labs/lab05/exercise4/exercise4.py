
def filter_query_times(times):
   mean = sum(times) / len(times)
   
   variance = sum ((t - mean) ** 2 for t in times) / len(times)
   std_ev = variance **(1/2)
   upper_limit = mean + std_ev

# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
