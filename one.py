with open('one.txt') as f:
    lines = f.readlines()

elf_calories_totals = []
current = 0
for l in lines:
    if  l == '\n':
        elf_calories_totals.append(current)
        
        current = 0
    else:
        current += int(l)

elf_calories_totals.sort(reverse=True)
# Part 1

print(elf_calories_totals[0])

# Part 2

print(sum(elf_calories_totals[0:3]))