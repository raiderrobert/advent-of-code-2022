
with open('four.txt') as f:
    lines = f.readlines()


# part 1
items = []

# example: 2-4,6-8
# for l in lines:
#     first, second = l.split(',')
#     first_start, first_end = first.split('-')
#     second_start, second_end = second.split('-')

#     if int(first_start) <= int(second_start) <= int(second_end) <= int(first_end):
#         items.append(1)
#         print(f"{l}")
#     elif int(second_start) <= int(first_start) <= int(first_end) <=int(second_end):
#         items.append(1)
#         print(f"{l}")

# print(sum(items))


# part 2
items = []

# example: 2-4,6-8
for l in lines:
    first, second = l.split(',')
    first_start, first_end = first.split('-')
    second_start, second_end = second.split('-')

    if int(first_start) <= int(second_start) <= int(first_end):
        items.append(1)
    elif int(first_start) <= int(second_end) <= int(first_end):
        items.append(1)
    elif int(second_start) <= int(first_start) <= int(second_end):
        items.append(1)
    elif int(second_start) <= int(first_end) <= int(second_end):
        items.append(1)
    else:
        print(l)


print(sum(items))