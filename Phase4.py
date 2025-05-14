import random

# Function to simulate one part's measurement
def measure_part(target, tolerance):
    return round(random.gauss(target, tolerance / 2), 2)

# Function to inspect a batch of parts
def inspect_batch(sample_size, target_length, tolerance):
    pass_count = 0
    fail_count = 0
    parts = []

    for i in range(sample_size):
        length = measure_part(target_length, tolerance)
        result = "PASS" if abs(length - target_length) <= tolerance else "FAIL"
        parts.append((i + 1, length, result))

        if result == "PASS":
            pass_count += 1
        else:
            fail_count += 1

    return parts, pass_count, fail_count

# Parameters
sample_size = 20         # Number of parts to inspect
target_length = 10.0     # Target length in cm
tolerance = 0.2          # ±0.2 cm allowed

# Run inspection
parts, passed, failed = inspect_batch(sample_size, target_length, tolerance)

# Display results
print("Item | Length (cm) | Result")
for item_id, length, result in parts:
    print(f"{item_id:>4} | {length:>11} | {result}")

# Summary
print("\nSummary:")
print(f"Total: {sample_size}, Passed: {passed}, Failed: {failed}")
