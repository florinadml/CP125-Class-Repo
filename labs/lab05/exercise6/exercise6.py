
def find_slow_endpoints(api_calls, threshold):
    """
    Find endpoints with average response time exceeding threshold.
    Only considers successful requests (status 200).
    Endpoint must have at least 2 successful calls.
    
    Args:
        api_calls: List of tuples (endpoint, response_time_ms, status_code)
        threshold: Maximum acceptable average response time in ms
    
    Returns:
        Sorted list of slow endpoint names
    """
    pass


# Test
api_calls = [
    ("/login", 45, 200), 
    ("/login", 120, 200), 
    ("/data", 80, 200),
    ("/login", 50, 500),
    ("/data", 95, 200), 
    ("/search", 30, 200),
    ("/health", 150, 200)
]

result = find_slow_endpoints(api_calls, 70)
print(f"Slow endpoints: {result}")  # Expected: ["/data", "/login"]
