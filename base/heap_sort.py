# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : heap_sort.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/26 20:31
------------------------------------------
堆排序
"""


def sift(data, low, high):
    """
        堆调整函数
        data: list
        low:  堆的根节点位置
        high: 堆的最后一个元素的位置，防止由父节点找子节点时候越界
    """
    # i 最开始指向根节点
    i = low

    # 左节点
    j = i * 2 + 1

    # 把堆顶存起来
    tmp = data[low]

    # # 只要 j 位置有数，就一直进行比较，直到比较完成为止
    while j <= high:

        # 取子节点数值大的那个先进行比较
        # 若右子节点比较大，则 j 指向右节点
        # Tips：j + 1 <= high, 保证没有越界
        # 整句解释就是: 如果 右子节点有并且比左节点大，那么，j 就指向右节点
        if j + 1 <= high and data[j + 1] > data[j]:
            j = j + 1

        # 若子节点最大的值比较大，则将子节点的值放入父节点的位置
        if data[i] > tmp:
            data[i] = data[j]

            # 往下看一层
            # 该选子节点(当前j所指向的节点)的值了，看看tmp能不能放进去
            i = j
            j = i * 2 + 1

        # 否则，tmp比任何子节点都大，将tmp放入父节点位置
        else:
            # 因为这里有一个data[i] = tmp, while条件不满足的时候也有一个 data[i] = tmp，所以，这俩简化，这里注释掉，运行外边的
            # data[i] = tmp
            break

    data[i] = tmp


def heap_sort(data):
    """
        堆排序
    """
    n = len(data)

    # 1. 创建堆
