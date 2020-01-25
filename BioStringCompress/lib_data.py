import os
import re

def translateRNAToDNA(sequence:list) -> list:
    return ['T' if base=='U' else base for base in sequence]

def translateDNAToRNA(sequence:list) -> list:
    return ['U' if base=='T' else base for base in sequence]

def _checkPathdirExist(filepath:str, create:bool = False):
    dirpath = os.path.dirname(filepath)
    if not os.path.isdir(dirpath) and dirpath != "":
        if create:
            os.makedirs(dirpath)
        else:
            raise FileNotFoundError(f'{dirpath} does not exist.')


def readBinary(filename:str) -> list:
    _checkPathdirExist(filename)
    with open(filename, 'rb') as datafile:
        data = datafile.read()
    return [byte for byte in data]

def readNormal(filename:str) -> list:
    _checkPathdirExist(filename)
    with open(filename, 'r') as datafile:
        data = datafile.read().upper()
    return re.findall('.*?[ACGTRYSWKMBDHVN-]', data)


def writeBinary(filename:str, data:list):
    _checkPathdirExist(filename, create=True)
    with open(filename, 'wb+') as datafile:
        datafile.write(bytes(data))

def writeNormal(filename:str, data:list):
    _checkPathdirExist(filename, create=True)
    data = "".join(data)
    with open(filename, 'w+') as datafile:
        datafile.write(data)
