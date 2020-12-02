import re

with open('input.txt') as f:
    data = f.read().strip().splitlines()

def parse_line(line):
    m = re.search(
        r'(\d+)-(\d+) ([a-z]): ([a-z]+)',
        line
    )

    policy_min = int(m.group(1))
    policy_max = int(m.group(2))
    policy_char = m.group(3)
    password = m.group(4)

    count = password.count(policy_char)
    return policy_min <= count and count <= policy_max


valid = 0
for line in data:
    if parse_line(line):
        valid += 1

print(valid)
