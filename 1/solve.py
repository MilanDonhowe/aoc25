def solve(file):
    with open(file, 'r') as chal:
        # part 1: code golf mode
        combos = chal.read().strip().split('\n')
        s=50
        acc=0
        for combo in combos: 
            s = (s + int(combo[1:]) if combo[0] == 'R' else s - int(combo[1:])) % 100
            acc += int(s == 0)
        # part 2: naive approach
        s2=50
        acc2=0
        for combo in combos:
            for _ in range(0, int(combo[1:])):
                if combo[0] == 'R':
                    s2 = (s2 + 1) % 100
                else:
                    s2 = (s2 - 1) % 100
                if s2 == 0:
                    acc2 += 1
        return acc, acc2

print('test: %d, %d' % solve('test_input'))
print('input: %d, %d' % solve('input'))
