def find_duplicate(nums):
    nums.sort()

    for i in range(len(nums) - 1):
        j = i + 1

        num1 = nums[i]
        num2 = nums[j]

        if not isinstance(num1, int) or num1 < 0:
            return False

        if num1 == num2:
            return num1

    return False
