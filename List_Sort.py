# -*- coding: utf-8 -*-
"""
Project Description: The "advanced_sort" function will take a list of elements and return a list with the items from the 
original list stored into sublists. Each sublist will contain items of the same value.

Function Paramters: advanced_sort("list of elements")

Sample Input: advanced_sort([2, 1, 2, 1])
    
Sample Output: [[2, 2], [1, 1]]

"""

def process_list(lst, temp_list, new_list):
    
    first_element = lst[0]
    
    for elm in lst:
        if elm == first_element:
            temp_list.append(elm)
            
    new_list.append(temp_list)

def advanced_sort(lst):

    new_list = []
    temp_list = []
    
    process_list(lst, temp_list, new_list)
    
    while True:
    
        if len(lst) == len(temp_list):
            return new_list
        else:
            while temp_list[0] in lst:
                lst.remove(temp_list[0])

            temp_list = []
            
            process_list(lst, temp_list, new_list)
            
            