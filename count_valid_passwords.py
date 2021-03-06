# Count valid passwords in pw_input accordign to rules:
# 3-4 b: wgzbpwpbj  Min 3  'b's, max 4 'b's - Invalid
# 1-6 z: mzzzbrzz  Min 1 'z's max 6 'z's - Valid
import re


def check_password(min_val, max_val, char, password):
    char_count = password.count(char)
    if char_count >= int(min_val) and char_count <= int(max_val):
        return True

    return False


pw_input = []
with open('pw_input', 'r') as f:
    pw_input = f.read().split('\n')

valid_pws = 0

for line in pw_input:
    matches = re.search(r"(\d+)-(\d+)\s+(\w):\s+(\w+)", line).groups()
    if check_password(*matches):
        valid_pws += 1

print(valid_pws)
