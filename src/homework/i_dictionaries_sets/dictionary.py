# #
# def get_p_distance(list1, list2):
#     indx = 0
#     diff = 0
#     while indx < len(list1):
#         if list1[indx] != list2[indx]:
#             diff += 1
#         indx += 1
#     p_distance = diff / len(list1)
#     return p_distance

# def get_p_distance_matrix(list1):
#     p_distance_matrix = []
#     for row_list in list1:
#         row = []
#         for column_list in list1:
#             row.append(get_p_distance(row_list, column_list))
#         p_distance_matrix.append(row)
#     return p_distance_matrix
list1 = [['T', 'G', 'A', 'A', 'G', 'T', 'A', 'C', 'G', 'T'], 
['T', 'G', 'T', 'A', 'G', 'T', 'A', 'C', 'G', 'T'], 
['A', 'C', 'A', 'A', 'G', 'T', 'A', 'C', 'G', 'T'], 
['A', 'G', 'T', 'A', 'G', 'T', 'A', 'C', 'G', 'T']]
list2 = ['T', 'G', 'T']
def get_p_distance(list1, list2):
    i = 0
    _diff_ = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            _diff_ += 1
        i += 1
    p_distance = _diff_ / len(list1)
    return p_distance

def get_p_distance_matrix(list1):
    p_distance_matrix = []
    for l_row in list1:
        row = []
        for l_column in list1:
            column = []
            row.append(get_p_distance(l_row, l_column))
            column.append(get_p_distance(l_row, l_column))
        p_distance_matrix.append(row)
    return p_distance_matrix

