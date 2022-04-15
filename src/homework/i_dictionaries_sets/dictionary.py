
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

# Dave also helped me with this via GroupMe

def add_inventory(widgets):
    quantity = 0
    w = 'widget_name'
    widgets = {}
    widg_dict = {'widget_name':30}
    if widgets[w] not in widgets:
        widgets.update(widg_dict)
        quantity += 1
    else:
        print('Error')

def remove_inventory_widget(widget_name):
    dictionary1 = {'widget1':30, 'widget2':40}
    dictionary_len = len(dictionary1)
    if dictionary1['widget1'] in dictionary1:
        dictionary1.pop('widget1')
    else:
        return 'item not found'