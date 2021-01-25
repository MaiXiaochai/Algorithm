# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : quick_sort.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/25 16:37
------------------------------------------
    快速排序
    时间复杂度: O(nlogn), 每一层的时间复杂度为 O(n)，一共有 logn层，所以，时间复杂度为 O(nlogn)
"""
from random import choice


def partition(data: list, left: int, right: int):
    """
        @param data: 要操作的列表
        @param left: 要操作的列表的开始位置
        @param right: 要操作的列表的结束位置
        时间复杂度: O(n)
    """
    # 快速排序是任意选择一个，现在是将任意认为规定为第一个
    # 腾出"空盒子"

    # 容易出现最坏情况
    # 随机取值，极大概率降低最坏情况出现概率
    tmp = data[left]

    while left < right:

        # 从右边找比tmp小的数
        while left < right and data[right] >= tmp:
            # 向左走一步
            right -= 1

        # 找到了比 tmp小的数，将数从此刻 right指向的盒子中拿出来，放到之前 tmp所在的盒子
        data[left] = data[right]

        while left < right and data[left] <= tmp:
            left += 1

        # 把找到的数从左边的盒子中拿出来，放到右边空缺空盒子中
        data[right] = data[left]

    # 把 tmp归位
    # 这里最后 left = right, 写哪个都行
    data[left] = tmp

    return left


def quick_sort(data: list, left: int, right: int):
    """
        快速排序
    """
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


def demo():
    li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
    quick_sort(li, 0, len(li) - 1)
    print(li)


if __name__ == '__main__':
    demo()
