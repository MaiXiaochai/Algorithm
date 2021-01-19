# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : hanoi.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/18 22:01
------------------------------------------
汉诺塔
"""
times = 0


def hanoi(number, a, b, c):
    """
        n 多少个盘子
        a, b, c 均为柱子名称
        含义：n个盘子从 a 经过 b 移动到 c

        假设移动 x盘子需要 h(x)步，分三步
    """

    if number > 0:
        # 1. 将 n-1个盘子看为一个整体，从 a 经过 c 移动到 b
        # 公式：h(n-1)
        hanoi(number - 1, a, c, b)

        # 2. 将第 n个盘子移动到 c
        # 公式：+1
        print(f"{a} --> {c}")

        # 3. 将 n-1个盘子看为一个整体，从 b 经过 a 移动到 c
        # 公式: h(n-1)
        hanoi(number - 1, b, a, c)

    # 所以，h(x) = 2h(x-1) + 1


if __name__ == '__main__':
    n = 2
    hanoi(n, 'A', 'B', 'C')
