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


def bubble_sort(lis):
    """
        1.冒泡排序
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
        2.选择排序
    """
    for i in range(len(lis) - 1):
        min_loc = i
        for j in range(i, len(lis)):
            if lis[j] < lis[min_loc]:
                min_loc = j

        if min_loc != i:
            lis[i], lis[min_loc] = lis[min_loc], lis[i]

    print(f"选择排序: {lis}")


def insert_sort(data: list):
    """
        插入排序
    """
    for i in range(1, len(data)):
        # 无序区抽出来的数
        tmp = data[i]

        # 有序区最右边的数的位置
        j = i - 1

        while data[j] > tmp and j >= 0:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = tmp

    print(f"插入排序: {data}")


def partition(data, left, right):
    """
        归位函数-快速排序用
    """
    # 基准数(pivot), [a, b, ..., p, ..., y, z]
    p = data[left]

    while left < right:
        # 找比 p小的数放到左边空位
        while left < right and p <= data[right]:
            right -= 1

        data[left] = data[right]

        while left < right and p >= data[left]:
            left += 1

        data[right] = data[left]

    # 把 p值放到中间
    data[left] = p

    return left


def partition_pro(data, left, right):
    """
        归位函数-快速排序用
    """


def quick_sort(data, left, right):
    """
        快速排序
    """
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)

    print(data)


def demo_low(lis):
    funcs = [
        bubble_sort,
        select_sort,
        insert_sort,
    ]
    for no, func in enumerate(funcs, 1):
        func(d_copy(lis))


if __name__ == '__main__':
    # will_sort = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    will_sort = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    # demo_low(will_sort)
    quick_sort(will_sort, 0, len(will_sort) - 1)
