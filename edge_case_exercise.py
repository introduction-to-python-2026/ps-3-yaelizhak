def move(my_list, direction=None):
    index_of_one = my_list.index(1)
    new_list = my_list.copy()
    if index_of_one == (len(my_list)-1) and direction == "right":
        return new_list
    elif index_of_one == 0 and direction == "left":
        return new_list

    if direction == 'right':
        new_list[index_of_one] = 0
        new_list[index_of_one + 1] = 1
    elif direction == 'left':
        new_list[index_of_one] = 0
        new_list[index_of_one - 1] = 1
    
    return new_list

def approximate_pi(n_terms):
  libneiz_list = []
  for n in range(1,11,):
    libneiz_list.append((-1)**n/(2*n+1))
    y = sum(libneiz_list)
    x = y*4
    return(x)
