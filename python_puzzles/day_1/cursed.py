result = (f := open("inputs/day1.txt"), n := [int(line) for line in f], f.close(), sum(sum(cur < nxt for cur, nxt in zip(n[offset::3], n[offset+3::3])) for offset in range(3)))[-1]

print(result)
