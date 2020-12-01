with open('input.txt') as f:
    data = [int(x) for x in f.read().strip().splitlines()]

print(
    sum([
        (m // 3) - 2
        for m in data
    ])
)
