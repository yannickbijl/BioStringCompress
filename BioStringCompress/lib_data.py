import os

def _check_pathdir_exist(filepath:str, create:bool = False):
    dirpath = os.path.dirname(filepath)
    if not os.path.isdir(dirpath):
        if create:
            os.makedirs(dirpath)
        else:
            raise FileNotFoundError


def read_binary(filename:str):
    _check_filepath_exist(filename)
    with open(filename, 'rb') as datafile:
        pass
    return data


def read_normal(filename:str):
    _check_filepath_exist(filename)
    with open(filename, 'r') as datafile:
        pass
    return data


def write_binary(filename:str):
    _check_filepath_exist(filename, create=True)
    with open(filename, 'wb+') as datafile:
        pass
    return data


def write_normal(filename:str):
    _check_filepath_exist(filename, create=True)
    with open(filename, 'w+') as datafile:
        pass
    return data
