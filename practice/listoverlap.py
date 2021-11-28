# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
finall = []
for item in a:
    if (item in b) and ( item not in finall):
        finall.append(item)

print(finall)


#with this you can just create new list but with duplicates
result = [i for i in a if i in b]
print(result)

#To eradicate duplicates we can use set()
results = [i for i in set(a) if i in b]
print(results)

#or you can use .count function
result_overlaps = [i for i in a if i in b]
print(result_overlaps)
results = [i for i in result_overlaps if result_overlaps.count(i) == 1]
print(results)