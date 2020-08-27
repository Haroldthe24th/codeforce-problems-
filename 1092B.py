def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def int_put():
    num_list = input("").split()
    
    return [int(input) for input in num_list]

st_num = int(input(""))
skill_list = int_put()
skill_list.sort()
#go through the list find the nearest number to what the current index is
#increment it if need be so it's == to curr
ex_num = 0
def find_ex_num(skill_li):
    global ex_num
    #list exhausted return from fo
    if(len(skill_li) == 0):
        return
    curr_skill = skill_li[0]
    skill_li.remove(curr_skill)
    closest_num = closest(skill_li, curr_skill)
    skill_li.remove(closest_num)

    if(closest_num == curr_skill):
        return find_ex_num(skill_li)
    else:
        ex_num += abs(closest_num - curr_skill)
        return find_ex_num(skill_li)
            


find_ex_num(skill_list)
print(ex_num)
