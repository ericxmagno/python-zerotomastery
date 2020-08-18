def highest_even(li):
    li.reverse()
    for item in li:
        if item % 2 == 0:
            return item
    return None

print(highest_even([10,3,6,7,8,12,1]))