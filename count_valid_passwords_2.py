# Count valid passwords in pw_input accordign to rules:
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.


import re


def check_password(has_char, not_char, char, password):
    if password[int(has_char) - 1] is char and \
            password[int(not_char) - 1] is not char:
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
