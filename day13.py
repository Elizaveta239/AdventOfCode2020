from typing import List, Tuple


def read_data1(filename: str):
    with open(f"input/{filename}") as f:
        text = f.read()
        lines = text.split("\n")
        start = int(lines[0])
        buses = lines[1].split(",")
        buses = list(filter(lambda x: x != "x", buses))
        buses = list(map(lambda x: int(x), buses))
        return start, buses


def find_rem(start: int, buses: List[int]):
    min_rem = buses[0] - start % buses[0]
    min_bus = buses[0]
    for bus in buses:
        rem = start % bus
        if rem == 0:
            return bus, 0
        else:
            if bus - rem < min_rem:
                min_rem = bus - rem
                min_bus = bus
    return min_rem, min_bus


def task1():
    start, buses = read_data1("input13.txt")
    wait_time, bus = find_rem(start, buses)
    print(wait_time, bus)
    print(wait_time * bus)


def read_data2(filename: str):
    with open(f"input/{filename}") as f:
        text = f.read()
        lines = text.split("\n")
        start = int(lines[0])
        buses = lines[1].split(",")
        return start, buses


def prepare_buses(buses: List[str]):
    bus_time = []
    for i in range(0, len(buses)):
        if buses[i] != "x":
            bus = int(buses[i])
            bus_time.append((bus, (bus - i) % bus))

    return bus_time


def get_r(a: List[int]):
    r = []
    for i in range(0, len(a)):
        r.append([])
        for j in range(0, len(a)):
            if j > i and a[i] != 0:
                r[i].append((a[i] ** (a[j] - 2)) % a[j])
            else:
                r[i].append(0)
    return r


def find_time(bus_time: List[Tuple[int, int]]):
    # Chinese remainder theorem
    x = []
    p = [bus_time[i][0] for i in range(0, len(bus_time))]
    a = [bus_time[i][1] for i in range(0, len(bus_time))]
    r = get_r(p)
    for i in range(0, len(bus_time)):
        x.append(a[i])
        for j in range(0, i):
            x[i] = r[j][i] * (x[i] - x[j])

        x[i] = x[i] % p[i]
        if x[i] < 0:
            x[i] += p[i]

    mul = 1
    ans = x[0]
    for i in range(1, len(x)):
        next = x[i]
        mul *= p[i - 1]
        ans += next * mul
    print(x)
    return ans


def task2():
    start, buses = read_data2("input13.txt")
    bus_time = prepare_buses(buses)
    print(find_time(bus_time))


if __name__ == "__main__":
    task1()
    task2()
