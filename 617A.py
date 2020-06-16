import math
dis = int(input(""))

steps = [5,4,3,2,1]
dis_by_step = []
for step in steps:
    dis_by_step.append(math.ceil(dis / step))
    
print(dis_by_step[0])