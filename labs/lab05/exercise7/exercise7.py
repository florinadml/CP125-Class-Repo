
def find_conflicting_ports(rules):
    """
    Find ports with conflicting rules (both ALLOW and BLOCK).
    Returns the port and the rule ID that created the conflict.
    
    Args:
        rules: List of tuples (rule_id, port, action)
    
    Returns:
        Sorted list of tuples (port, conflicting_rule_id)
    """
    pass


# Test 1
rules = [
    (1, 80, "ALLOW"), 
    (2, 443, "ALLOW"), 
    (3, 80, "BLOCK"),
    (4, 22, "BLOCK"), 
    (5, 443, "BLOCK"), 
    (6, 8080, "ALLOW")
]

result = find_conflicting_ports(rules)
print(f"Conflicts: {result}")  # Expected: [(80, 3), (443, 5)]


# Test 2
rules2 = [
    (1, 80, "ALLOW"), 
    (2, 80, "ALLOW"), 
    (3, 443, "BLOCK")
]

result2 = find_conflicting_ports(rules2)
print(f"Conflicts: {result2}")  # Expected: []
