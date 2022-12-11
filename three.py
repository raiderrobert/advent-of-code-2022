import string

with open('three.txt') as f:
    lines = f.readlines()

LETTER_SCORE = { l: i  for i, l in enumerate(string.ascii_letters, 1)}

# part 1
# items = []

# for l in lines:
#     first = l[:len(l)//2]
#     second = l[len(l)//2:]
#     common_item = list(set(first) & set(second))[0]
#     item_score = LETTER_SCORE.get(common_item)
#     items.append(item_score)
# print(sum(items))

# part 2
items = []

for x, y, z in zip(*[iter(lines)]*3):
    print(x,y,z)
    one, two, three = set(x.replace('\n', '')), set(y.replace('\n', '')), set(z.replace('\n', ''))
    print(one, two, three)
    common_item = list(one & two & three)[0]
    item_score = LETTER_SCORE.get(common_item)
    items.append(item_score)
    print(f'{common_item}: {item_score}')
print(sum(items))