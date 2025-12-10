def calculate_allowances(transport,meal):
    transport = 200.00
    meal = 150.00
    return transport + meal

def calculate_overtime(base_salary, overtime_hours):
    hourly_rate = base_salary / 160  # Assuming 160 working hours per month
    overtime_rate = hourly_rate * 1.5  # 1.5x for overtime
    return overtime_hours * overtime_rate

def calculate_epf(gross_salary):
    return gross_salary * 0.11

def calculate_socso(gross_salary):
    return gross_salary * 0.02

def calculate_net_salary(base_salary, overtime_hours):
    # Step 1: Calculate gross salary
    allowances = calculate_allowances()
    overtime = calculate_overtime(base_salary, overtime_hours)
    gross = base_salary + allowances + overtime
    
    # Step 2: Calculate deductions
    epf = calculate_epf(gross)
    socso = calculate_socso(gross)
    
    # Step 3: Calculate net
    net = gross - epf - socso
    return net

# Use it
salary = calculate_net_salary(5000, 10)
print(f"Net salary: RM{salary:.2f}")