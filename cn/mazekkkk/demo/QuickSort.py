#coding=utf-8
# 快速排序 复杂度（n * log n）
def quicksort(array):
    # 基准条件: 如果数组长度小于2直接返回
    if len(array) < 2:
        return array
    # 递归条件: 选择基准值，根据基准值分为小于基准值的数组和大于基准值的数组，通过递归调用小于基准值的条件 + 基准值 + 递归调用大于基准值的条件实现排序
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10,7,3,6,777,123,123123,123123,123134444,5555987234,12983718972])
