# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
   if vehicle_type == "Electric" :
      return 2.00
   elif vehicle_type == "Hybrid" and (hour_24 >= 22 or hour_24 <= 6) :
      return 2.00
   elif vehicle_type == "Hybrid":
      return 5.00
   else:
      return 5.00
   
print("Testing Dynamic Parking Rate...")
