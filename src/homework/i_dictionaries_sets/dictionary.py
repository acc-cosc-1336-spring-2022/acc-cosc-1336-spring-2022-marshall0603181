#
list2 = []
list3 = []
list4 = []
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
    for row_list in list1:
        row = []
        for column_list in list1:
            row.append(get_p_distance(row_list,column_list))
        p_distance_matrix.append(row)
    return p_distance_matrix

