from typing import List


def read_data(filename: str):
    with open(f"input/{filename}") as f:
        lines = f.readlines()
        nums = map(lambda x: int(x.strip()), lines)
        return list(nums)


def get_two_numbers_with_sum(nums: List[int], sum):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == sum:
                return i, j


def find_first_num(nums, p):
    for i in range(p, len(nums)):
        res = get_two_numbers_with_sum(nums[i - p: i], nums[i])
        if res is None:
            return i


def task1():
    nums = read_data("input9.txt")
    ind = find_first_num(nums, 25)
    print(f"Answer is {nums[ind]}, index: {ind}")


def get_set_with_sum(nums, sum):
    for start in range(0, len(nums)):
        temp_sum = nums[start]
        for end in range(start + 1, len(nums)):
            temp_sum += nums[end]
            if temp_sum == sum:
                return start, end
            elif temp_sum > sum:
                break


def task2():
    nums = read_data("input9.txt")
    ind = find_first_num(nums, 25)
    sum = nums[ind]
    start, end = get_set_with_sum(nums, sum)
    set_nums = nums[start: end + 1]
    print(f"Indexes are: {start}, {end}. Answer is {min(set_nums) + max(set_nums)}")


if __name__ == "__main__":
    task1()
    task2()
