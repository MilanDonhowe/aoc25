import re
def solve(file):
    with open(file, 'r') as f:
        ranges=[tuple(map(int, line.split('-'))) for line in f.read().split(',')]
        # p1
        s = 0
        for (a, b) in ranges:
            for x in range(a, b+1, 1):
                rep = str(x)
                if (len(rep) & 1) == 0:
                    if rep[0:(len(rep)//2)] == rep[len(rep)//2:]:
                        s += x
        # p2 regex for repeats
        s2 = 0
        for (a, b) in ranges:
            for x in range(a, b+1, 1):
                rep = str(x)
                # need ^ and $ delimiter to ensure no digit that's not part of a duplicate
                if re.search(r"^(?P<common>\d+)(?P=common)+$", rep):
                    s2 += x
        return s, s2


print('test: %d, %d' % solve('test_input'))
print('input: %d, %d' % solve('input'))
