def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        value_max = my_list[0]
        for nm in my_list:
            if nm > value_max:
                value_max = nm
    return value_max
