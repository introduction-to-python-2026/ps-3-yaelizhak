def estimate_pi (num_of_points):
  inside_circle = 0
  outside_circle = 0
  num_of_points = 1001
  for i in range(num_of_points):
    import random
    x = random.random ()
    import random
    y = random.random ()
    r = 0.5
    distance_to_center = ((y-r)**2+(x-r)**2)**0.5 #r=0.5
    if distance_to_center<=r: 
      inside_circle +=1
    if distance_to_center>r:
      outside_circle +=1

  pi = 4*inside_circle/num_of_points
  return pi


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


