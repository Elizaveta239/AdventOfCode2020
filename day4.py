import re


fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

class PassportData:
    def __init__(self):
        self.info = {key: None for key in fields}

    def __repr__(self):
        return str(self.info)


def parse_data(lines):
    passports = []
    for passport_data in lines:
        fields = re.split(" |\n", passport_data)
        passport = PassportData()
        for field in fields:
            if field != "":
                field_data = field.split(":")
                name, value = field_data[0], field_data[1]
                if name in passport.info.keys():
                    passport.info[name] = value
                else:
                    print(f"Strange field: {name}")
        passports.append(passport)
    return passports


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.read()
        lines = lines.split("\n\n")
        return parse_data(lines)


def is_valid(passport):
    for key, val in passport.info.items():
        if val is None and key != "cid":
            return False
    return True


def check_valid(passports):
    res = 0
    invalid_passports = []
    for passport in passports:
        if is_valid(passport):
            res += 1
        else:
            invalid_passports.append(passport)
    return res, invalid_passports


def task1():
    passports = read_data("input4.txt")
    ans, inlavid = check_valid(passports)
    print(f"Answer is {ans}")
    print("Inlavid passports are:")
    for p in inlavid:
        print(p)


def is_field_valid(name, value):
    if name in ['byr', 'iyr', 'eyr']:
        try:
            value = int(value)
        except:
            return False
        if name == 'byr':
            return 1920 <= value <= 2002
        elif name == "iyr":
            return 2010 <= value <= 2020
        elif name == "eyr":
            return 2020 <= value <= 2030
    if name == "hgt":
        is_cm = False
        if value.endswith("cm"):
            value = value[:-2]
            is_cm = True
        elif value.endswith("in"):
            value = value[:-2]
        else:
            return False
        try:
            value = int(value)
        except:
            return False
        if is_cm:
            return 150 <= value <= 193
        else:
            return 59 <= value <= 76
    if name == "hcl":
        if len(value) != 7:
            return False
        matched = re.match("#([0-9][a-f])*", value)
        return bool(matched)
    if name == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if name == "pid":
        if len(value) != 9:
            return False
        return value.isdigit()


def check_full_valid(passports):
    res = 0
    invalid_passports = []
    for passport in passports:
        valid = True
        for key, val in passport.info.items():
            if (key != "cid") and (val is None or not is_field_valid(key, val)):
                valid = False
                break
        if valid:
            res += 1
        else:
            invalid_passports.append(passport)
    return res, invalid_passports


def task2():
    passports = read_data("input4.txt")
    ans, inlavid = check_full_valid(passports)
    print(f"Answer is {ans}")
    print("Inlavid passports are:")
    for p in inlavid:
        print(p)


if __name__ == "__main__":
    task1()
    task2()