#!/usr/bin/python3

import pyautogui
from time import sleep

def lil_chut(l_number, f_number):

    file_list1 = [(0,10), (10,15), (15,23), (23,31), (31,37), (37,50)]
    file_list2 = [(0,8), (8,17), (17,26), (26,38)]
    file_list3 = [(0,9), (9,24), (24,35), (35,47)]
    file_list4 = [(0,14), (14,31), (31,48), (48,66), (66,74)]
    file_list5 = [(0,8), (8,20), (20,33)]

    master_list1 = [file_list1, file_list2, file_list3, file_list4, file_list5]
    master_list2 = ["./sort_by_N.py", "./too_short.py", "./no_partial.py",
                   "./poly_a_tail.py", "./i_plot.py"]


    sleep(3)
    tuple_name = master_list1[l_number][f_number]
    the_start, the_end = tuple_name
    file_name = master_list2[l_number]
    ar_file = open(file_name, 'r')
    divide_it = ar_file.readlines()

    for line in divide_it[the_start:the_end]:
        pyautogui.write(line, interval=0.01)
        sleep(0.15)

    ar_file.close()

