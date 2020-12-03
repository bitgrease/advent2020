# Count valid passwords in pw_input accordign to rules:
# 3-4 b: wgzbpwpbj  Min 3  'b's, max 4 'b's - Invalid
# 1-6 z: mzzzbrzz  Min 1 'z's max 6 'z's - Valid
#
# Approach:
# read in file (each line is a list entry)
# Parse each line with regex to get min and max, pw
# Use those values to determine if line is valid or not based on parms
# Increment counter for each valid pw

