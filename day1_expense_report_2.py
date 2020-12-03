# Find the three values from puzzle_one_input file that totals 2020

TOTAL = 2020
expenses = []

with open('puzzle_one_input', 'r') as f:
    expenses = [int(value) for value in f.read().split('\n')]

for idx1 in range(len(expenses) - 2):
    for idx2 in range(1, len(expenses) - 1):
        for idx3 in range(2, len(expenses)):
            total = expenses[idx1] + expenses[idx2] + expenses[idx3]
            if total == TOTAL:
                print(f"value1 is {expenses[idx1]}")
                print(f"value2 is {expenses[idx2]}")
                print(f"value3 is {expenses[idx3]}")
                exit()
