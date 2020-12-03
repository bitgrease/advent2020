# Count valid passwords in pw_input accordign to rules:
# 3-4 b: wgzbpwpbj  Min 3  'b's, max 4 'b's - Invalid
# 1-6 z: mzzzbrzz  Min 1 'z's max 6 'z's - Valid
#
# Approach:
# read in file (each line is a list entry)
# Parse each line with regex to get min and max, pw
# Use those values to determine if line is valid or not based on parms
# Increment counter for each valid pw
import re

# Regex group #'s
MIN = 1
MAX = 2
CHAR = 3
PW = 4


def check_password(min, max, char, password):
    pass


pw_input = []
with open('pw_input', 'r') as f:
    pw_input = f.read().split('\n')

valid_pws = 0

for line in pw_input:
    matches = re.search(r"(\d)-(\d)\s+{w}:\s+(\w+)", line).groups()
    if check_password(*matches):
        valid_pws += 1

print(valid_pws)
