import os.path

def edit_file(file_name, file_write):
    f = open(file_name, "a")
    try:
        os.path.exists(file_name)
    except FileExistsError:
        file_name.open(file_name, "x")
    f.write(file_write)
    print(f.read(file_name))
    f.close()
    
def read_from_file(file_name):
    f = open(file_name, "r")
    try:
        os.path.exists(file_name)
    except FileExistsError:
        print("This file does not exist.")
    print(f.read())

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("The file does not exist.")