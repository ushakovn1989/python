src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

uniq_nums = set()
for num in src:
    if num in uniq_nums:
        uniq_nums.discard(num)
    else:
        uniq_nums.add(num)

uniq_nums_ord = [num for num in src if num in uniq_nums]
print(uniq_nums_ord)
