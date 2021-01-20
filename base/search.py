# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : search.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/20 21:30
------------------------------------------
"""
from cal_time import timer


@timer
def linear_search(lis, value):
    """
        顺序查找
        时间复杂度: O(n)
    """
    for ind, v in enumerate(lis):
        if v == value:
            return ind

    return None


@timer
def binary_search(lis, value):
    """
        二分查找
        时间复复杂度: O(logn)
    """
    left = 0
    right = len(lis) - 1

    while left <= right:
        # tips: Python 的整除是向负无穷方向取整
        mid = (left + right) // 2

        # 情况一：找到了
        if lis[mid] == value:
            return mid

        # 情况二：待查找的值在 mid左侧
        elif lis[mid] > value:
            right = mid - 1

        # 情况三：待查找的值在 mid右侧
        # lis[mid] < value
        else:
            left = mid + 1

    # 情况四：没找着
    return None


def demo():
    """
     P10 09:55
    """
    lis = list(range(10000))
    print("线性查找：", linear_search(lis, 3879))

    print("二分查找：", binary_search(lis, 3879))


if __name__ == '__main__':
    demo()
