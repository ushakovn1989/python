src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (num for num in src[1:] if num > src[src.index(num) - 1])

print(list(result))
