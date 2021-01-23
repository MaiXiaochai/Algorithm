# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : all_sort_in_one.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/23 20:06
------------------------------------------
"""
from copy import deepcopy as d_copy


# 算法默写，能写出来才是学会了

# 1. 冒泡排序
def bubble_sort(lis):
    """
        冒泡排序
    """
    for i in range(len(lis) - 1):
        exchange = False
        for j in range(len(lis) - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                exchange = True

        if not exchange:
            break

    print(f"冒泡排序: {lis}")


def select_sort(lis):
    """
        选择排序
    """
    for i in range(len(lis) - 1):
        min_loc = i
        for j in range(i, len(lis)):
            if lis[j] < lis[min_loc]:
                min_loc = j

        if min_loc != i:
            lis[i], lis[min_loc] = lis[min_loc], lis[i]

    print(f"选择排序: {lis}")


def demo(funcs, lis):
    for func in funcs:
        result = func(d_copy(lis))

        if result:
            print(result)


if __name__ == '__main__':
    # will_sort = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    will_sort = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    functions = [
        bubble_sort,
        select_sort,
    ]
    demo(functions, will_sort)
