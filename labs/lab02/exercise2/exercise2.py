# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
   tent_cost = math.ceil(participants / tent_capacity ) * tent_price
   total_budget = tent_cost + (meal_price * participants)
   return total_budget
# Test your code here
print("Testing Camping Logistics...")
