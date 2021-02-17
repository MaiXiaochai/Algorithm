# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : shell_sort.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/2/17 10:36
------------------------------------------
希尔排序(分组的插入排序)
"""


def insert_sort_gap(lis, gap):
    """
        插入排序
    """
    for i in range(1, len(lis)):
        # 摸到的牌的下标
        tmp = lis[i]

        # 分组之后是和不同组的相同位置去比，所以，i - gap
        # 同样，j也可以理解为手里的牌的下标
        j = i - gap

        while lis[j] > tmp and j >= 0:
            lis[j + gap] = lis[j]
            j -= gap

        lis[j + gap] = tmp


def shell_sort(lis):
    d = len(lis) // 2
    while d >= 1:
        insert_sort_gap(lis, d)
        d //= 2


if __name__ == '__main__':
    from random import shuffle

    li = list(range(10))
    shuffle(li)
    shell_sort(li)
    print(li)
