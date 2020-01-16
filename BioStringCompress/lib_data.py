import os
import re

def _check_pathdir_exist(filepath:str, create:bool = False):
    dirpath = os.path.dirname(filepath)
    if not os.path.isdir(dirpath) and dirpath != "":
        if create:
            os.makedirs(dirpath)
        else:
            raise FileNotFoundError(f'{dirpath} does not exist.')


def read_binary(filename:str) -> list:
    _check_pathdir_exist(filename)
    with open(filename, 'rb') as datafile:
        data = datafile.read()
    return [byte for byte in data]

def read_normal(filename:str) -> list:
    _check_pathdir_exist(filename)
    with open(filename, 'r') as datafile:
        data = datafile.read()
    return re.findall('.*?[ACGTRYSWKMBDHVN-]', data)


def write_binary(filename:str, data:list):
    _check_pathdir_exist(filename, create=True)
    with open(filename, 'wb+') as datafile:
        datafile.write(bytes(data))

def write_normal(filename:str, data:list):
    _check_pathdir_exist(filename, create=True)
    data = "".join(data)
    with open(filename, 'w+') as datafile:
        datafile.write(data)
