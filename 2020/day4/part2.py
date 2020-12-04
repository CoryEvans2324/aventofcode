import re

class Passport:
    def __init__(self, passport: str) -> None:
        self.byr = ''  # birth_year
        self.iyr = ''  # issue_year
        self.eyr = ''  # expire_year
        self.hgt = ''  # height
        self.hcl = ''  # hair_color
        self.ecl = ''  # eye_color
        self.pid = ''  # passport_id
        self.cid = ''  # country_id


        self.parse(passport)

    def parse(self, passport: str) -> None:
        passport = passport.replace('\n', ' ')

        for raw_kv in passport.split(' '):
            key, value = raw_kv.split(':')
            setattr(self, key, value)

    def is_valid(self):
        # return all([
        #     self.byr is not None,
        #     self.iyr is not None,
        #     self.eyr is not None,
        #     self.hgt is not None,
        #     self.hcl is not None,
        #     self.ecl is not None,
        #     self.pid is not None,
        #     self.cid is not None or True  # optional
        # ])

        # Birth Year
        try:
            if not (1920 <= int(self.byr) <= 2002):
                return False
        except (ValueError, TypeError) as e:
            return False

        # Issue Year
        try:
            if not (2010 <= int(self.iyr) <= 2020):
                return False
        except (ValueError, TypeError) as e:
            return False

        # Expire Year
        try:
            if not (2020 <= int(self.eyr) <= 2030):
                return False
        except (ValueError, TypeError) as e:
            return False

        # Height
        try:
            height_unit = self.hgt[-2:]
            height = int(self.hgt[:-2])

            if height_unit == 'cm' and \
                not (150 <= height <= 193):
                return False

            elif height_unit == 'in' and \
                not (59 <= height <= 76):
                return False

        except (ValueError, TypeError) as e:
            return False

        # Hair color
        if not (len(self.hcl) == 7 and re.match(r'#[0-9a-f]{6}', self.hcl)):
            return False

        # Eye color
        if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        # Passport ID
        if len(self.pid) != 9:
            return False
        try:
            int(self.pid)
        except (ValueError, TypeError) as e:
            return False

        return True


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
