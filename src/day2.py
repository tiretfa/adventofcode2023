def one_star():
    f = open('data/day2', 'r+')

    constraints = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    score = 0
    for line in f.readlines():
        game = int(line.split(':')[0].split(' ')[1])
        reveals = line.split(':')[1].split(';')
        possible = True
        for reveal in reveals:
            cubes = reveal.split(',')
            for cube in cubes:
                cube = cube.strip(' ')
                number = int(cube.split(' ')[0])
                color = cube.split(' ')[1].strip('\n')
                if constraints[color] < number:
                    possible = False
        if possible:
            score += game

    print(score)

def two_star():
    f = open('data/day2', 'r+')

    score = 0
    for line in f.readlines():
        reveals = line.split(':')[1].split(';')
        maxs = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for reveal in reveals:
            power = 1
            cubes = reveal.split(',')
            for cube in cubes:
                cube = cube.strip(' ')
                number = int(cube.split(' ')[0])
                color = cube.split(' ')[1].strip('\n')
                if maxs[color] < number:
                    maxs[color] = number
            
        for color, m in maxs.items():
            print(f'color : {color}, : {m}, power: {power}')
            power *= m
        score += power

    print(score)

two_star()