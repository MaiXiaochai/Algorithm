# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : bubble_sort.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/22 13:30
------------------------------------------
冒泡排序
"""


def bubble_sort(lis):
    """
        冒泡排序
        时间复杂度：O(n^2)
    """
    for i in range(len(lis)):  # 第 i 趟
        for j in range(len(lis) - i - 1):  # 指针位置
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]


def bubble_sort_pro(lis):
    """
        冒泡排序改进版
        改进思路:
                1) 有可能在进行到某一次的时候，整个列表已经排好序了，这个时候就不需要再进行后边的排序了
                2) 另一个角度，假如索引为 0的值是整个列表中最大的值，那么它只需要交换 len(lis) - 1 就能交换到 索引最大的位置,
                   每一趟，其实都是各个值在向上交换几个位置，最多 len(lis) - 1 次就能交换完
    """
    for i in range(len(lis) - 1):  # 第 i 趟
        exchange = False  # 是否有相邻的元素发生位置交换

        for j in range(len(lis) - i - 1):  # 指针位置
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                exchange = True

        if not exchange:
            break


def demo():
    lis = [1, 2, 7, 3, 6, 9, 5, 4, 8]
    # lis = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(lis)
    print(lis)


if __name__ == '__main__':
    demo()
