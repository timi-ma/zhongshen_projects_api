def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        # 标记是否发生了交换
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # 交换元素
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        # 如果没有交换，说明已经有序，提前结束
        if not swapped:
            break
    return lst


my_list = [64, 34, 25, 12, 22, 11, 90]
print("排序前:", my_list)
sorted_list = bubble_sort(my_list)
print("排序后:", sorted_list)
