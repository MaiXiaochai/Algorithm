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
from heapq import heapify, heappop
from random import shuffle


def sift(data, low, high):
    """
        堆(大根堆)调整函数
        data: list
        low:  堆的根节点位置
        high: 堆的最后一个元素的位置，防止由父节点找子节点时候越界
        时间复杂度：O(logn)
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
        if data[j] > tmp:
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


def sift_small_root(data, low, high):
    """
        堆(小根堆)调整函数
        data: list
        low:  堆的根节点位置
        high: 堆的最后一个元素的位置，防止由父节点找子节点时候越界
        时间复杂度：O(logn)
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
        if j + 1 <= high and data[j + 1] < data[j]:
            j = j + 1

        # 若子节点最大的值比较大，则将子节点的值放入父节点的位置
        if data[j] < tmp:
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
        时间复杂度：O(nlogn)
    """
    print(f"初始的乱序列表：{data}")
    n = len(data)

    # 1. 创建堆
    for i in range((n - 2) // 2, -1, -1):
        # i表示创建堆的时候，调整的部分的根的下标
        # 函数 sift中 high的作用是防止j超过边界，如果j不超过索引值为 n-1的high，就不会超过边界
        sift(data, i, n - 1)

    print(f"生成的堆：{data}")

    # 2.堆排序
    for j in range(n - 1, -1, -1):
        # 指向当前堆的最后一个元素
        data[0], data[j] = data[j], data[0]

        # j - 1 是新的 high
        sift(data, 0, j - 1)

    print(f"堆排序后的列表：{data}")


def topk(data: list, k):
    """
        Topk问题
    """
    heap_ = data[:k]

    # 1. 创建堆
    for i in range((k - 2) // 2, -1, -1):
        sift_small_root(heap_, i, k - 1)

    # 2. 遍历
    for j in range(k, len(data) - 1):
        if data[j] > heap_[0]:
            heap_[0] = data[j]
            sift_small_root(heap_, 0, k - 1)

    # 3. 挨个出数
    for x in range(k - 1, -1, -1):
        # 指向当前堆的最后一个元素
        heap_[0], heap_[x] = heap_[x], heap_[0]

        # j - 1 是新的 high
        sift_small_root(heap_, 0, x - 1)

    print(f"堆排序后的列表：{heap_}")


def demo():
    li = [i for i in range(100)]
    shuffle(li)
    topk(li, 10)


def demo2():
    """
        内置堆模块的使用
    """
    li = [i for i in range(100)]
    shuffle(li)
    heapify(li)

    # heappop 每次弹出堆中最小的数
    n = len(li)
    for i in range(n):
        print(heappop(li))


if __name__ == '__main__':
    demo()
    # demo2()
