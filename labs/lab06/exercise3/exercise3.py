def audit_blocklists(list_a, list_b, list_c):
    A = set(list_a)
    B = set(list_b)
    C = set(list_c)

    universal = A & B & C 
    redundant = ( A & B) | (A & C) | (B & C)
    unique_A = A - B - C 

    return (universal, redundant, unique_A)
