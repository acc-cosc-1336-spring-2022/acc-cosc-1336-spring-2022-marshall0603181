

def get_p_distance(list1, list2):
    indx = 0
    difference = 0
    while indx < len(list1):
        if list1[indx] != list2[indx]:
            difference += 1
        indx += 1
    p_distance = difference / len(list1)
    return p_distance

def get_p_distance_matrix(list1):
    p_distance_matrix = []
    for row_list in list1:
        row = []
        for column_list in list1:
            row.append(get_p_distance(row_list, column_list))
        p_distance_matrix.append(row)
    return p_distance_matrix