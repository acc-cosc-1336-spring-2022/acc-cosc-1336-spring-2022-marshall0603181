# def add_inventory_item(items, item_name, item_quantity):
#     if item_name not in items:
#         items[item_name] = item_quantity
#     else:
#         items[item_name] += item_quantity

# def display_inventory_item(items, item_name):
#     if item_name in items:
#         print(items[item_name])
#     else:
#         print('Item not found')

def write_to_file(file_name, file_write):
    f = open('C:/Users/marsh/acc_files/test.txt', "w")
    f.write(file_write)
    f.close()

def read_from_file(file_name):
    f = open(file_name, "r")
    print(f.read())