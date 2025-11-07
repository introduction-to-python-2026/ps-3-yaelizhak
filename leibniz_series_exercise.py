def approximate_pi(n_terms):
  libneiz_list = []
  for n in range(1,11,):
    libneiz_list.append((-1)**n/(2*n+1))
    y = sum(libneiz_list)
    x = y*4
    return(x)
