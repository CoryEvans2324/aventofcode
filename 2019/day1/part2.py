

def calc_fuel_for_module(mass):
    fuel = 0

    while True:
        req = (mass // 3) - 2
        if req <= 0:
            break

        fuel += req
        mass = req

    return fuel


with open('input.txt') as f:
    data = [int(x) for x in f.read().strip().splitlines()]

print(
    sum(
        map(calc_fuel_for_module, data)
    )
)
