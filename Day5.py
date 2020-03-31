# Loops and Iterations

# For Loops

nums = [1, 2, 3, 4]

for nums in nums:
    print(nums)
print("#########")

nums = [1, 2, 3, 4]

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

print('########')

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

print('##########')

# Nested Loop
for num in nums:
    for letter in 'abc':
        print(num, letter, end=' ')

print("\n")
# using range()

for i in range(10):
    print(i, end=' ')

print("\n")

for i in range(1, 11):
    print(i, end='')

print("\n")
# While loops

x = 0
while x < 10:
    print(x, end= '')
    x += 1

print("\n")

x = 0
while x < 10:
    if x == 5:
        break
    print(x, end='')
    x += 1


