def main():
    with open('input.txt') as f:
        data = f.read().strip().splitlines()

    numbers = [int(x) for x in data]

    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if i == j:
                continue

            if a + b == 2020:
                print(a, b, a * b)
                return

if __name__ == "__main__":
    main()
