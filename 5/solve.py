from collections import Counter
def solve(file):
  with open(file, 'r') as f:
    ids, items = f.read().strip().split('\n\n')
    ids = [tuple(map(int, id_range.split('-'))) for id_range in [id_range for id_range in ids.split('\n')]]
    # ranges start from min_start, max_start
    DB = [range(a, b+1) for a,b in sorted(ids, key=lambda x: x[0])]

    items = list(map(int, items.split('\n')))
    p1=0
    for item in items:
      for check in DB:
        if item in check:
          p1+=1
          break
    p2=0
    # count number of accepted ids
    # need to reduce our ranges into a set of disjoint ranges, then sum their spans
    i=1
    disjoint_DB = [DB[0]]
    while i < len(DB):
      # I already sorted the ranges by lower element in ascending order
      # so for two consecutive ranges: (a, b), (c, d)
      # so if c in (a, b) we can merge both ranges into (a, max(b,d))
      if DB[i].start in disjoint_DB[-1]:
        #  we can merge
        r0 = disjoint_DB.pop()
        disjoint_DB.append(range(r0.start, max(r0.stop, DB[i].stop)))
      else:
        # this is disjoint with existing ranges
        disjoint_DB.append(DB[i])
      i += 1
    # sanity check
    assert len(disjoint_DB) < len(DB)

    p2 = sum([r.stop - r.start for r in disjoint_DB])
    
    return p1, p2
print("test: %d, %d" % solve('test_input'))
print("input: %d, %d" % solve('input'))
