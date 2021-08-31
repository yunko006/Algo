def binary_search(array, n):
    
    find = False

    while not find:
        
        # moyenne de la list
        mid_index = len(array) // 2
        if len(array) != 0:
            mid_point = array[mid_index]

        else:
            return find

        if mid_point == n:
            find = True

        if n > mid_point:
            # cad on va vers la droite
            array = array[(mid_index+1):]

        elif n < mid_point:
            # cad on va vers la gauche 
            array = array[:(mid_index)]
        
    return find


if __name__ == '__main__':
    print(binary_search([1, 2, 7, 12, 43, 44, 54, 100, 124, 147], 54))
