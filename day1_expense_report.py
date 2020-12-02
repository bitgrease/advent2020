# Find the two values from puzzle_one_input file that totals 2020
# Return the product

TOTAL = 2020
current_values = []
test_value = ''

with open('puzzle_one_input', 'r') as f:
    current_values = f.read().split('\n')

for value in current_values:
    test_value = TOTAL - int(value)

    if str(test_value) in current_values:
        break

print(f"{value} + {test_value} = {int(value) + int(test_value)}.")
print(f"The product of the two numbers is {test_value * int(value)}")

