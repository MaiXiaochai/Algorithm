# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : merge_sort.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/2/2 14:45
------------------------------------------
"""


def merge(li, low, mid, high):
    """
        归并函数
    """
    i = low
    j = mid + 1
    l_tmp = []

    # 只要左右两边都有数
    while i <= mid and j <= high:
        if li[i] < li[j]:
            l_tmp.append(li[i])
            i += 1

        else:
            l_tmp.append(li[j])
            j += 1

    while i <= mid:
        l_tmp.append(li[i])
        i += 1

    while j <= high:
        l_tmp.append(li[j])
        j += 1

    # 列表指定切片也可以赋值
    li[low: high + 1] = l_tmp


def merge_sort(li, low, high):
    """
        归并排序
        思想：
            1）选一个中间位置，左边放比它小的数，右边放比它大的数
            2）当只有两个数时，依然可以进行比较，只有一个数的时候，这里默认分到右边
            3）递归进行
    """
    # 至少有两个元素, 递归
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


if __name__ == '__main__':
    data = [2, 4, 5, 7, 9, 1, 3, 6, 8]
    merge_sort(data, 0, 8)
    print(data)
