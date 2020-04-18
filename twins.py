n =input("")
sn =input("")

min_cn = 0
accum = 0

sn_list = [int(k) for k in sn.split(' ')]
sn_list.sort(reverse=True)
sn_list_dup = sn_list.copy()

for x in range(len(sn_list)):
    if(accum > sum(sn_list_dup)):
        break
    accum += sn_list_dup.pop(0)
    min_cn += 1

    
print(min_cn)
    