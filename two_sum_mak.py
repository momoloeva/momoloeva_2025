def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_sorted(nums, target):
    indexed_nums = [(num, idx) for idx, num in enumerate(nums)]
    indexed_nums.sort(key=lambda x: x[0])
    
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        if current_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

def two_sum_hashmap(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]
    
    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}")
        print(f"O(N²): {two_sum_brute_force(nums, target)}")
        print(f"O(N log N): {two_sum_sorted(nums, target)}")
        print(f"O(N): {two_sum_hashmap(nums, target)}")
        print()
