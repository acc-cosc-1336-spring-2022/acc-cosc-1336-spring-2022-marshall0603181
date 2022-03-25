def loop_list_w_for(num):
    for n in num:
        print(n)

def loop_list_w_while(num):
    i = 0
    while i < 4:
        print(num)
        i += 1

def collect_home_values():
    home_values = [0] * 5
    indx = 0
    while indx < len(home_values):
        home_values[indx] = int(input('input home value: '))
        indx += 1

    for v in home_values:
        print(v)

def append_item_to_list(item1, list1):
    list1.append(item1)