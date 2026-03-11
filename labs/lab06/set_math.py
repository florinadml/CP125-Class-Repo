# Visitors to different sections
homepage_visitors = {"user_1", "user_2", "user_3", "user_4"}
checkout_visitors = {"user_3", "user_4", "user_5", "user_6"}

# 1. Intersection (&): Who visited BOTH? (Loyal Users)
loyal = homepage_visitors & checkout_visitors
print(f"Loyal Users: {loyal}")

# 2. Difference (-): Who visited the homepage but NEVER reached checkout? (Lost Sales)
lost_sales = homepage_visitors - checkout_visitors
print(f"Lost Conversions: {lost_sales}")

# 3. Symmetric Difference (^): Who visited only ONE page (either home or checkout, but not both)?
one_pagers = homepage_visitors ^ checkout_visitors
print(f"Single Page Visitors: {one_pagers}")

# 4. Union (|): What is our total unique audience across both pages?
total_audience = homepage_visitors | checkout_visitors
print(f"Total Unique Reach: {total_audience}")