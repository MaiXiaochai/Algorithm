# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : select_sort.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/22 14:58
------------------------------------------
选择排序
"""


def select_sort(lis):
    """
        1. 选择排序
        2. 缺点：
                1) 需要额外新的列表，多占一份内存
                2) 时间复杂度：O(n^2)
        3. 关键点:
                1) 有序区和无序区的划分，巧妙划分
                2) 无序区最小数的位置(索引)
    """
    li_new = []
    for i in range(len(lis)):  # 第 i遍选择
        min_val = min(lis)  # min 是O(n)
        li_new.append(min_val)  # remove O(n)
        lis.remove(min_val)

    return li_new


def select_sort_pro(lis):
    """
        选择排序，加强版
        思路：用一个列表，把该列表分为有序区和无序区，然后将选出的最小与有序的尾部的第一个无序区元素交换位置即可
    """
    # 剩下最后的一个数的时候，它和自己比肯定是最小的，所以，len(lis) - 1
    for i in range(len(lis) - 1):
        # 1.假设无序区最小值位置为 i（每次的无序区是[i:]）
        min_loc = i

        # 3. 步骤2中，j从 i 开始，第一次是 i和 i比，有点浪费，能省一次就省一次，所以，j从 i + 1开始
        for j in range(i + 1, len(lis)):
            # 2.
            if lis[j] < lis[min_loc]:
                min_loc = j

        if min_loc != i:
            # 4. 当前无序区第一个值和当前无序区最小值做交换，交换后，当前无序区第一个值变为了整体的有序区的一部分
            lis[i], lis[min_loc] = lis[min_loc], lis[i]


def demo():
    lis = [1, 2, 7, 3, 6, 9, 5, 4, 8]
    select_sort_pro(lis)
    print(lis)


if __name__ == '__main__':
    demo()
