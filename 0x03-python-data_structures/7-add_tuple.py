#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = 0
    b = 0
    for j in tuple_a:
        if j == tuple_a[0]:
            a = a + j
        elif j == tuple_a[1]:
            b = b + j
    for i in tuple_b:
        if i == tuple_b[0]:
            a = a + i
        elif i == tuple_b[1]:
            b = b + i
    return (a, b)
