def binary_search(array, n):
    
    find = False

    while not find:
        
        # moyenne de la list
        mid_index = len(array) // 2
        mid_point = array[mid_index]

        if len(array) == 2 and mid_point != n:
            print(f"{n} not in array")
            find = True

        if mid_point == n:
            find = True

        if n > mid_point:
            # cad on va vers la droite
            array = array[(mid_index+1):]

        elif n < mid_point:
            # cad on va vers la gauche 
            array = array[:(mid_index)]
        

binary_search([1, 2, 7, 12, 43, 44, 54, 100, 124, 147], 42)
