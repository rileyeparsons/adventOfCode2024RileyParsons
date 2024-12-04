import re
import math

def get_input():
    target = './day3/input.txt'
    # target = './day3/test.txt'
    # target = './day3/test2.txt'
    with open(target, 'r') as input:
        lines = [line.rstrip('\n') for line in input.readlines()]
    return lines

def find_sequences(line):
    reg = r'mul\(\d+,\d+\)'
    return re.findall(reg, line)

def extract_values(mul):
    return re.findall(r'\d+', mul)

def find_adv_sequences(line):
    reg = r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)'
    return re.findall(reg, line)

def check_mul(line):
    if re.match(r'mul', line):
        return True
    return False

def extract_adv_values(input):
    if re.match(r'do', input):
        if re.match(r'don\'t()', input):
            return False
        else:
            return True

def part1():
    lines = get_input()
    sum = 0
    for line in lines:
        sequences = find_sequences(line)
        for mul in sequences:
            vals = [int(x) for x in extract_values(mul)]
            sum = sum + math.prod(vals)
    return sum

def part2():
    lines = get_input()
    sum = 0
    enabled = True
    for line in lines:
        sequences = find_adv_sequences(line)
        for mul in sequences:
            if enabled and check_mul(mul):
                vals = [int(x) for x in extract_values(mul)]
                sum = sum + math.prod(vals)
            else:
                if(extract_adv_values(mul)):
                    enabled = True
                else:
                    enabled = False
    return sum

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()