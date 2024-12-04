def get_input():
    target = './day2/input.txt'
    # target = './day2/test.txt'
    with open(target, 'r') as input:
        lines = [line.rstrip('\n') for line in input.readlines()]
    return lines

def check_safety(report, dampen = False):
    for i in range(len(report)-1):
        change = report[i+1]-report[i]
        if abs(change) != 2 and abs(change) != 1 and abs(change) != 3:
            if dampen:
                for j in range(len(report)):
                    dampened_report = report[:j] + report[j+1:]
                    if check_safety(dampened_report):
                        return True
            return False
        if i > 0:
            prev = report[i] - report[i-1]
            if prev*change < 0:
                if dampen: 
                    for j in range(len(report)):
                        dampened_report = report[:j] + report[j+1:]
                        if check_safety(dampened_report):
                            return True
                return False
    return True

def part1():
    lines = get_input()
    safe = 0
    for line in lines:
        report = [int(x) for x in line.split()]
        if check_safety(report):
            safe += 1
    return safe

def part2():
    lines = get_input()
    safe = 0
    for line in lines:
        report = [int(x) for x in line.split()]
        if check_safety(report, dampen=True):
            safe +=1
    return safe

def main():
    print(part1())
    print(part2())

if __name__ == '__main__':
    main()