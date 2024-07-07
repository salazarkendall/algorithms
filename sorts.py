def bubble_sort(my_list: list) -> list:
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


def selection_sort(my_list: list) -> list:
    for i in range(len(my_list)-1):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[min_idx] > my_list[j]:
                min_idx = j
        if min_idx != i:
            aux = my_list[i]
            my_list[i] = my_list[min_idx]
            my_list[min_idx] = aux
    return my_list


def insertion_sort(my_list) -> list:
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


def merge(l1, l2) -> list:
    combined = []
    while l1 and l2:
        if l1[0] < l2[0]:
            combined.append(l1.pop(0))
        else:
            combined.append(l2 .pop(0))
    return combined + (l1 or l2)


def merge_sort(l):
    if len(l) == 1:
        return l
    mid_index = int(len(l)/2)
    left = merge_sort(l[:mid_index])
    right = merge_sort(l[mid_index:])
    return merge(left, right)


def swap(l, i1, i2):
    temp = l[i1]
    l[i1] = l[i2]
    l[i2] = temp


def pivot(l, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if l[i] < l[pivot_index]:
            swap_index += 1
            swap(l, swap_index, i)
    swap(l, pivot_index, swap_index)
    return swap_index


def __quick_sort(l, left, right):
    if left < right:
        pivot_index = pivot(l, left, right)
        __quick_sort(l, left, pivot_index-1)
        __quick_sort(l, pivot_index+1, right)
    return l

def quick_sort(l):
    return __quick_sort(l, 0, len(my_list)-1)

my_list = [4, 6, 1, 7, 3, 2, 5]
quick_sort(my_list,)

print(my_list)

# print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
