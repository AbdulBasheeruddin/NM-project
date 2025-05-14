# Tolerance ranges
length_range = (9.0, 10.2)
width_range = (4.8, 5.2)

# Simulated measurements
length = 10.3
width = 5.0

# Check quality
length_ok = length_range[0] <= length <= length_range[1]
width_ok = width_range[0] <= width <= width_range[1]

if length_ok and width_ok:
    print("Product: PASS")
else:
    print("Product: FAIL")
