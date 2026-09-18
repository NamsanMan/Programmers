def solution(nums):
    answer = 0
    N = len(nums)
    new_nums = []
    for i in range(len(nums)):
        if nums[i] not in new_nums:
            new_nums.append(nums[i])
    
    if len(new_nums) >= N / 2:
        return (N / 2)
    elif len(new_nums) < N / 2:
        return len(new_nums)
    
    
    return answer