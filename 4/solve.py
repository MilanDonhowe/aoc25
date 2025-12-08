def solve(file):
    with open(file, 'r') as f:
        layout = list(map(list, f.read().strip().split('\n')))
        width = len(layout[0])
        height = len(layout)
        grid_0 =[[0 for _ in range(width)] for __ in range(height)]
        
        
        def take_rolls(grid):
            # i'm too lazy to do bounds detection, let exception handling save me    
            def check(j, k):
                try:
                    # stupid negative index wrap-around bug fix
                    if (j < 0) or (k < 0):
                        return 0
                    return int(layout[j][k] == '@')
                except IndexError:
                    return 0
            # pass 1: count neighbors
            for i in range(0, height, 1):
                for ii in range(0, width, 1):
                    if layout[i][ii] != '@':
                        grid[i][ii]=float('inf')
                        continue
                    grid[i][ii] += check(i-1, ii)
                    grid[i][ii] += check(i-1, ii-1)
                    grid[i][ii] += check(i-1, ii+1)
                    grid[i][ii] += check(i, ii+1)
                    grid[i][ii] += check(i, ii-1)
                    grid[i][ii] += check(i+1, ii)
                    grid[i][ii] += check(i+1, ii-1)
                    grid[i][ii] += check(i+1, ii+1)
            # pass 2 remove rolls
            acc = 0
            for i in range(0, height, 1):
                for ii in range(0, width, 1):
                    if grid[i][ii] < 4:
                        acc += 1
                        layout[i][ii] = '.'
            return acc
        
        p1 = take_rolls(grid_0)

        # part 2:
        p2 = p1
        while True:
            # need to reinit score grid onh each iteration
            add = take_rolls([[0 for _ in range(width)] for __ in range(height)])
            if add == 0:
                break
            p2 += add

        return p1, p2
                
print('test: %d, %d' % solve('test_input'))
print('input: %d, %d' % solve('input'))
