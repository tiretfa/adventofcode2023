import re 

def one_star(line):
    first_num = None
    last_num = None
    first = True
    for c in line:
        if c.isdigit():
            if first:
                first_num = c
                first = False
            last_num = c
    return int(first_num + last_num)

reg = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

def get_num(num):
    try:
        return {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }[num]
    except Exception:
        return num

f = open("data/day1.txt", "r")
sum = 0
for line in f.readlines():
    numbers = re.findall(reg, line)
    sum += int(get_num(numbers[0]) + get_num(numbers[-1]))
print(sum)