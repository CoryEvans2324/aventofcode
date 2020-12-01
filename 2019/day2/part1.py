with open('input.txt') as f:
    data = [int(x) for x in f.read().strip().split(',')]

def add(current_index, int_list):
    a_index = int_list[current_index + 1]
    b_index = int_list[current_index + 2]
    r_index = int_list[current_index + 3]

    a = int_list[a_index]
    b = int_list[b_index]

    int_list[r_index] = a + b

def multiply(current_index, int_list):
    a_index = int_list[current_index + 1]
    b_index = int_list[current_index + 2]
    r_index = int_list[current_index + 3]

    a = int_list[a_index]
    b = int_list[b_index]

    int_list[r_index] = a * b


program = data.copy()

index = -4  # start on -4 to keep loop clean (2nd inter -> index = 0, opcode = progam[0])
opcode = 0
while opcode != 99:
    if opcode == 1:
        add(index, program)

    if opcode == 2:
        multiply(index, program)

    index += 4
    opcode = program[index]

print(program[0])
