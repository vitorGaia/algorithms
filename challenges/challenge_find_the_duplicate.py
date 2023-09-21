def find_duplicate(nums):
    encountered_nums = set()

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False

        if num in encountered_nums:
            return num

        encountered_nums.add(num)

    return False
