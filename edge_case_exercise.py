def move(my_list, direction=None):
    if not my_list or 1 not in my_list:
        return my_list.copy()  
        
    index_of_one = my_list.index(1)
    new_list = my_list.copy()
    
    if direction == "left" and index_of_one > 0:
        new_list[index_of_one] = 0
        new_list[index_of_one - 1] = 1
    elif direction == "right" and index_of_one < len(my_list) - 1:
        new_list[index_of_one] = 0
        new_list[index_of_one + 1] = 1
    
    return new_list


def approximate_pi(n_terms):
    total = 0
    for n in range(n_terms):
        total += (-1)**n / (2*n + 1)
    
    return round(4 * total, 4)
