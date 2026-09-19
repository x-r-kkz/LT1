# CHLOE SOPHIA IRENEO | 8 - CAMIA
# Circular Garden LT1

import math

# INPUT STAGE
radius = float(input("Please enter the radius of the garden (in meters): ")) # asks for radius to be used for calculations

# PROCESSING STAGE
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
root_area = math.sqrt(area)
floor_area = math.floor(area)
ceiling_area = math.ceil(area)

# OUTPUT STAGE
print(f"Area of the garden: {area:.2f} square meters \n"
      f"Circumference of the garden: {circumference:.2f} meters\n"
      f"Square root of the area: {root_area:.2f}\n"
      f"Area rounded down: {floor_area:.2f} square meters\n"
      f"Area rounded up: {ceiling_area:.2f} square meters") # :.2f only displays 2 decimal places
