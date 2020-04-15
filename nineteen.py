s = input("")
d = { 'n': 0, 'i': 0, 'e': 0, 't': 0}

for c in s:
    try:
        d[c] += 1
    except:
        pass

d['n']= (d['n']-1)//2
d['e']= d['e']//3

cnt = min(d.values())
if cnt < 0:
 cnt=0
print(cnt)
