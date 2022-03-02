def test_config():
    return True

def local_variable(val0):
    val = val0
    val0 = 100
    return val
    

def main(val0):
    val = 0
    local_variable(val0)