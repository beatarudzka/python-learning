# Print elements less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []

for nums in a:
    if nums < 5:
        new_list.append(nums)
        print(new_list)
