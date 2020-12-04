

class Passport:
    def __init__(self, passport: str) -> None:
        self.byr = None  # birth_year
        self.iyr = None  # issue_year
        self.eyr = None  # expire_year
        self.hgt = None  # height
        self.hcl = None  # hair_color
        self.ecl = None  # eye_color
        self.pid = None  # passport_id
        self.cid = None  # country_id


        self.parse(passport)

    def parse(self, passport: str) -> None:
        passport = passport.replace('\n', ' ')

        for raw_kv in passport.split(' '):
            key, value = raw_kv.split(':')
            setattr(self, key, value)

    def is_valid(self):
        return all([
            self.byr is not None,
            self.iyr is not None,
            self.eyr is not None,
            self.hgt is not None,
            self.hcl is not None,
            self.ecl is not None,
            self.pid is not None,
            self.cid is not None or True  # optional
        ])


def main():
    with open('input.txt') as f:
        data = f.read().strip()

    passports_raw = data.split('\n\n')
    passports = []
    for p in passports_raw:
        passports.append(Passport(p))

    valid_count = 0
    for p in passports:
        if p.is_valid():
            valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    main()
