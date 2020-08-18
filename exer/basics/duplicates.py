some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

# # set solution
# some_set = set(some_list)
# for letter in some_set:
#     if some_list.count(letter) > 1:
#         duplicates.append(letter)

# solution
for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in duplicates:
            duplicates.append(letter)

print(duplicates)