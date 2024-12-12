# Add two lists using map and lambda
numbers1 = [1, 2, 3, 15, 7]
numbers2 = [9, 5, 6, 8, 10]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists")
print(list(result))

#using map
nums = [1, 2, 3, 4, 5, 7, 22]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in lists")
print(square)