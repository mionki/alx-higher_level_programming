#!/usr/bin/python3
def element_at(my_list, idx):
    my_list = []
    for idx in range(len(my_list)-1):
        print("Element at index {:d} is {}".format(idx,my_list[idx]))
        if idx < 0:
            return None
        if idx > len(my_list):
            return None    