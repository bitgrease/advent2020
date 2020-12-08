reference_line = ''
lines = []
with open('slope_input', 'r') as f:
    lines = f.read().split()


slope_matrix[0][0] = lines.pop(0)
row = 1
for line in lines:
    if line == slope_matrix[0][0]:
        row = 0
        slope_matrix[row].append(line)
    else:
        slope_matrix[row].append(line)
    row += 1

print(slope_matrix)


