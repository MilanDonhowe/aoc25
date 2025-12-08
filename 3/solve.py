from time import time

def solve(file):
    t0 = time()

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
        
        # part 2: code monkey optimized this so it just barely works
        # I did initially write a recursive function, then unrolled it
        # into this for loop structure, but needed to add short-circuit
        # conditions to get this to execute in a reasonable amount of time (< 1 minute).
        def maxjolts(b):
            stk=[]
            # alright memoized version
            max_digit = max(b)
            stk=[(b, [])]
            
            
            best_combo = 0
            best_combo_str = '0'

            # I was going to add prefix short-circuit but didn't need it
            best_prefixes = {}
            while len(stk) > 0:
                # timeout kill
                if time()-t0 > 60:
                    print("demasiado despacio")
                    exit(0)

                seq, combo = stk.pop()


                if len(combo) == 12:
                    combo = int(''.join(map(str, combo)))
                    if combo > best_combo:
                        best_combo = int(combo)
                        best_combo_str = str(best_combo)
                    continue
                
                # drop useless branches
                if len(seq) + len(combo) < 12:
                    continue

                if len(seq) == 0:
                    continue

                # short circuit conditions
                
                # kill this branch if better one exists already
                if best_combo > 0:
                    # prefix check
                    prefix = int(best_combo_str[:len(combo)])
                    if prefix > int(''.join(map(str,combo))):
                        continue

                # checks how many more characters we can pick if we drop seq[0]
                qty_left   = len(seq[1:]) - len(combo)

                # how many more digits needed to complete a valid combination
                qty_needed = 12 - len(combo) 

                # look-ahead kills (reduce number of new branches created)

                # Always pick max digit if possible.  It is always optimal choice.
                if seq[0] == max_digit:
                    stk.append( (seq[1:], combo + [seq[0]]) )
                    continue

                if qty_left > qty_needed:
                    # if we have a 1 digit here
                    # we ignore it iff there's enough other digits to pick
                    # since they'll be guaranteed to be at least as good as 1
                    if seq[0] == 1:
                        stk.append( (seq[1:], combo) )
                        continue
                    

                stk.append( (seq[1:], combo + [seq[0]]) )
                stk.append( (seq[1:], combo) )
            return best_combo
        p2 = sum([maxjolts(battery) for battery in banks])

        return p1, p2



print("test: %d, %d" % solve('test_input'))
print("input: %d, %d" % solve('input'))