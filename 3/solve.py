def solve(file):
    with open(file, 'r') as f:
        # part 1
        banks=[list(map(int, list(x))) for x in f.read().strip().split('\n')]
        def maxjolts(b):
            # map all combination
            combos = [list(zip([x]*len(b[i+1:]), b[i+1:])) for i, x in enumerate(b)]
            # flatten list
            combos = [combo for combolist in combos for combo in combolist]
            t= max([(a*10) + b for a,b in combos])
            return t
        p1 = sum([maxjolts(battery) for battery in banks])
        
        # part 2
        def maxjolts(b):
            stk=[]
            # insane recursion time
            def build(bank, combo=[]):
                if len(combo) == 12:
                    stk.append(combo)
                    return
                if len(bank) == 0:
                    return
                build(bank[1:], combo+[bank[0]])
                build(bank[1:], combo)
            # build(b)
            # alright memoized version
            stk=[(b, [])]
            combos=[]
            while len(stk) > 0:
                seq, combo = stk.pop()
                if len(combo) == 12:
                    combos.append(combo)
                    continue
                if len(seq) == 0:
                    continue
                stk.append( (seq[1:], combo + [seq[0]]) )
                stk.append( (seq[1:], combo) )
            
            t = max([int(''.join(map(str, c))) for c in combos])
            return t
        p2 = sum([maxjolts(battery) for battery in banks])

        return p1, p2



print("test: %d, %d" % solve('test_input'))
print("input: %d, %d" % solve('input'))