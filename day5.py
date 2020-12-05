class Pass:
    def __init__(self, row, column):
        self.row = row
        self.column = column


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        result = []
        for line in lines:
            line = line[:-1]
            p = Pass(line[:-3], line[-3:])
            result.append(p)
        return result


def convert_to_number(seq, left: int, right: int, low_letter: str, up_letter: str):
    for letter in seq:
        l = (right - left + 1) // 2
        if letter == low_letter:
            right = right - l
        elif letter == up_letter:
            left = left + l
    if left == right:
        return left
    else:
        raise ValueError(f"The process isn't finished! {left} {right}")


def get_id(p: Pass):
    row_num = convert_to_number(p.row, 0, 127, "F", "B")
    column_num = convert_to_number(p.column, 0, 7, "L", "R")
    print(f"row: {row_num}, column: {column_num}")
    return row_num * 8 + column_num


def task1():
    passes = read_data("input5.txt")
    ans = []
    for p in passes:
        id = get_id(p)
        ans.append(id)
    print(f"Answ̵̵̵er is {max(ans)}")
    return ans


def task2():
    seats = task1()
    all = [i for i in range(0, max(seats))]
    all_set = set(all)
    seats_set = set(seats)
    missing_seats = all_set - seats_set
    print(f"Missing seats: {missing_seats}")
    suspect = max(missing_seats)
    if (suspect - 1) in seats_set and (suspect + 1) in seats_set:
        print(f"The answer is {suspect}")


if __name__ == "__main__":
    task1()
    task2()
