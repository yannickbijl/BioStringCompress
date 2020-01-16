def _intToBaseDict() -> dict:
    allBases = ["A", "C", "G", "T", "R", "Y", "S", "W", "K", "M", "B", "D", 
                "H", "V", "N", "-"]
    d = dict([(x,y) for x,y in enumerate(sorted(set(allBases)))])
    # d = {0: '-', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'G', 6: 'H', 7: 'K', 8: 'M', 9: 'N', 10: 'R', 11: 'S', 12: 'T', 13: 'V', 14: 'W', 15: 'Y'}
    return d

def _intToBase(integer:int, dictBases:dict) -> str:
    return dictBases[integer]

def _intToBitConversion(intConvBase: int) -> str:
    return format(intConvBase, '#010b')[2:]

def binDecompress(data:list = [28, 53]) -> list:
    seqList = []
    dictBases = _intToBaseDict()
    for byte in data:
        byte = _intToBitConversion(byte)
        seqList.append(int(byte[:4], 2))
        seqList.append(int(byte[4:], 2))
    return [_intToBase(base, dictBases) for base in seqList]


def countDecompress(data:list = ['1A', '1T', '1C', '1G']) -> list:
    print(data)


def binCountDecompress(data:list = [1, 12, 3, 5]) -> list:
    print(data)
