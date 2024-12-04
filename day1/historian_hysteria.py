import re

def get_input():
    target = './day1/input.txt'
    # target = './day1/test.txt'
    with open(target, 'r') as input:
        lines = [line.rstrip('\n') for line in input.readlines()]
    return lines

def get_numbers(line):
    re_number = r'\d+(?: \d+)?'
    found_numbers = re.findall(re_number, line)
    return found_numbers

def part1():
    lines = get_input()
    column1 = []
    column2 = []
    for line in lines:
        numbers = get_numbers(line)
        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))

    distances = []
    while len(column1) > 0 and len(column2) > 0:
        distances.append(abs(min(column1) - min(column2)))
        column1.remove(min(column1))
        column2.remove(min(column2))

    return sum(distances)

def part2():
    lines = get_input()
    dict = {}
    column1 = []
    column2 = []
    for line in lines:
        numbers = get_numbers(line)
        column1.append(int(numbers[0]))
        column2.append(int(numbers[1]))

    for val in column1:
        if(val in dict.keys()):
            dict[val] = dict[val] + (val * column2.count(val))
        else:
            dict[val] = val * column2.count(val)

    return sum(dict.values())

def main():
    print(part1())
    print(part2())
if __name__ == '__main__':
    main()