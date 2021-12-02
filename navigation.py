
input = 'inputs/day2_input.txt'

def displacement(input_file):
    position = [0, 0]
    with open(input_file) as file:
        for line in file:
            line_parts = line.split(' ')
            if line_parts[0] == 'forward':
                position[0] += int(line_parts[1])
            if line_parts[0] == 'down':
                position[1] += int(line_parts[1])
            if line_parts[0] == 'up':
                position[1] -= int(line_parts[1])

    return position[0] * position[1]

def disp_aim(input_file):
    position = [0, 0]
    aim = 0

    with open(input_file) as file:
        for line in file:
            line_parts = line.split(' ')
            if line_parts[0] == 'forward':
                mag = int(line_parts[1])
                position[0] += mag
                position[1] += mag * aim
            if line_parts[0] == 'down':
                aim += int(line_parts[1])
            if line_parts[0] == 'up':
                aim -= int(line_parts[1])

    return position[0] * position[1]

print(disp_aim(input))