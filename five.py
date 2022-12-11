import pprint

with open('five.txt') as f:
    lines = f.readlines()


# part 1
parsing_map = True
map_width= len(lines[0])//4
map_stacks = [[]for i in range(map_width)]

movement = []

class Command:
    def __init__(self, count, start, end):
        self.count = count
        self.start = start
        self.end = end

    def __str__(self):
        return f'move {self.count} from {self.start} to {self.end}'

for l in lines:
    line_len = len(l)

    if parsing_map is True and l[0] == '[':
        labels = l[1::4]
        for i, label in enumerate(labels):
            if label != ' ':
                map_stacks[i].append(label)

    if parsing_map is False:
        m = l.split()
        movement.append(Command(int(m[1]), int(m[3])-1, int(m[5])-1))

    if line_len == 1:
        parsing_map = False


def process_movement_one_at_a_time(command: Command):
    for i in range(command.count):
        box = map_stacks[command.start].pop(0)
        map_stacks[command.end].insert(0,box)

def process_movement_preserving_order(command: Command):
    items = []
    for i in range(command.count):
        box = map_stacks[command.start].pop(0)
        items.append(box)
    for i in reversed(items):
        map_stacks[command.end].insert(0,i)  

print("#### START ###")
pprint.pprint(map_stacks)

for i, command in enumerate(movement):
    log = i in (0,1)
    if log:
        print(command)
    process_movement_preserving_order(command)
    if log:
        pprint.pprint(map_stacks)


print("#### END ###")
pprint.pprint(map_stacks)
output = []
for i, stack in enumerate(map_stacks):
    top = stack[0:][0]
    print(i, top)
    output.append(top)

print("".join(output))
