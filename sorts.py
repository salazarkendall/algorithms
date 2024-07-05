def bubble_sort(my_list) -> list:
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
        for j in range(i+1, len(my_list)-1):
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


print(insertion_sort([4, 2, 6, 5, 1, 3]))
