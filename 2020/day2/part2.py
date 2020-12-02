import re

with open('input.txt') as f:
    data = f.read().strip().splitlines()

def parse_line(line):
    m = re.search(
        r'(\d+)-(\d+) ([a-z]): ([a-z]+)',
        line
    )

    policy_first_index = int(m.group(1))
    policy_next_index = int(m.group(2))
    policy_char = m.group(3)
    password = m.group(4)

    count = 0
    if password[policy_first_index - 1] == policy_char:
        count += 1

    if password[policy_next_index - 1] == policy_char:
        count += 1

    return count == 1


valid = 0
for line in data:
    if parse_line(line):
        valid += 1

print(valid)
