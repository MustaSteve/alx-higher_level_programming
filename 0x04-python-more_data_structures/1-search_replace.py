#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_newlist_i = []
    for array in my_list:
        if array == search:
            my_newlist_i.append(replace)
        else:
            my_newlist_i.append(array)
    return my_newlist_i
