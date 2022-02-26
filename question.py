def find_max(nums):
    max_num= float("-inf")

    for num in nums:
        if num > max_num:
            max_num=num
    return max_num
x_list=[23,45,6,1,6]
print(find_max(x_list))