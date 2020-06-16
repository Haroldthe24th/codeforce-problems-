def int_put():
    num_list = input("").split()
    
    return [int(input) for input in num_list]


#length of routes
d1,d2,d3 = int_put()

int_list = []
#possible routes that could be taking
r_1 = d1*2 + d2*2
r_2 = d1 + d2 + d3
r_3 = d1 + d3 * 2 + d1
r_4 = d2 + d3 * 2 + d2
#appendig them to list
int_list.append(r_1)
int_list.append(r_2)
int_list.append(r_3)
int_list.append(r_4)
#sorting it in acending order
int_list.sort()
#printing the smallest one(first one)
print(int_list[0])

