# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : insert_sort.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/25 11:53
------------------------------------------
插入排序
    理解：1）像是玩扑克牌的时候整理自己手中的牌，将每一张要判断的牌按大小顺序放到合适的位置
         2）每次从无序区拿出一张，然后插入有序区最左边开始的部分区域
         3）每次从有序区右边向左边开始判断，比待插入数大的向右挪，直到比待小的或者到左边第一位置停止，然后将待插入数插入安序合适位置
    时间复杂度: O(n^2)
"""


def insert_sort(lis):
    """
        插入排序
    """
    for i in range(1, len(lis)):  # 摸到的牌原来在手中牌中的索引
        tmp = lis[i]  # 摸到的牌

        # 在 while循环的第一个 j + 1 的位置的数据，是被摸到的 tmp这个张牌的值, 摸到就是被抽出去了，位置空着，可以被覆盖
        j = i - 1  # 有序区最右边的数的位置
        while lis[j] > tmp and j >= 0:
            lis[j + 1] = lis[j]
            j -= 1

        lis[j + 1] = tmp  # 这里的 j + 1 和 while循环中的 j -= 1 完美配合，准确地将数填到 "空盒子" 里


def demo():
    lis = [1, 2, 7, 3, 6, 9, 5, 4, 8]
    # lis = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    insert_sort(lis)
    print(lis)


if __name__ == '__main__':
    demo()
