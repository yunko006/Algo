def binary_search(array, n):

    mid_index = (len(array) - 1) // 2
    if len(array) != 0:
        mid_point = array[mid_index]
    else:
        return False

    if n == mid_point:
        return True

    if n > mid_point:
        array = array[(mid_index+1):]
        # print(array)
        return binary_search(array, n)

    elif n < mid_point:
        array = array[:mid_index]
        # print(array)
        return binary_search(array, n)
    

if __name__ == '__main__':
    print(binary_search([1, 2, 7, 12, 43, 44, 54, 100, 124, 147], 0))
