def main():
    with open('input.txt') as f:
        data = f.read().strip().splitlines()

    numbers = [int(x) for x in data]

    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            for k, c in enumerate(numbers):
                if any([i == j, i == k, k == j]):
                    continue

                if a + b + c == 2020:
                    print(a, b, c, a * b * c)
                    return


if __name__ == "__main__":
    main()
