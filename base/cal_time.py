# -*- encoding: utf-8 -*-

"""
------------------------------------------
@File       : cal_time.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2021/1/20 21:58
------------------------------------------
"""
from time import perf_counter


def timer(func):
    """
        计算函数运行时间的装饰器
    """

    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        time_cost = end - start

        print(f"{func.__name__} running time: {time_cost} secs")
        return result

    return wrapper
