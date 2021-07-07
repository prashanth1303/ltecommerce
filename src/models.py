import os
def file_exits(filename):
    return os.path.exista(filename) and os.path.isfile(filename)
    