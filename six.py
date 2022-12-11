with open('six.txt') as f:
    lines = f.readlines()

def start_checker(start_len, offset=0):
    for i in range(len(l)+1):
     look = l[i+offset:start_len+i+offset]
     if len(set(look)) == start_len:
        return i+start_len+offset

for l in lines:
    packet_step = 4

    packet_start = start_checker(packet_step)
    print(packet_start)

    message_step = 14
    message_start = start_checker(message_step, packet_start)
    print(message_start)


