# Find the three values from puzzle_one_input file that totals 2020
# Return the product

# Subtract first value from 2020 result stored as test value
# Subtract first value idx +1 from test value - remainder is new test value
# see if new test is in array.
# if not, repeat with next entry in the list.

# Alternate
# First + 2 + 3
# First + 2 + 4
# First + 3 + 4


TOTAL = 2020
expenses = []
value1 = ''
value2 = ''
value3 = ''

with open('puzzle_one_input', 'r') as f:
    current_values = [int(value) for value in f.read().split('\n')]


print(current_values)
