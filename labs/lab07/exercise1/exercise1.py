def process_actions(catalog, actions):
    for action, isbn in actions :
        if action == "BORROW":
            if isbn in catalog and catalog[isbn] > 0:
                catalog[isbn] -= 1
            else:
                return "ERROR"
        elif action == "RETURN" :
            if isbn in catalog:
                catalog[isbn] += 1
            else:
                return "error"
    return catalog

catalog = {
    "978-A": 2,
    "978-B": 0,
    "978-C": 1,
}
actions = [
    ("BORROW", "978-A"),
    ("BORROW", "978-A"),
    ("BORROW", "978-B"),
    ("RETURN", "978-B"),
    ("BORROW", "978-Z"),
]
result = process_actions(catalog, actions)
print(result)
