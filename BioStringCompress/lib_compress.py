def _baseToIntDict():
    allBases = ["A", "C", "G", "T", "R", "Y", "S", "W", "K", "M", "B", "D", 
                "H", "V", "N", "-"]
    d = dict([(y,x) for x,y in enumerate(sorted(set(allBases)))])
    # d = {'-': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'G': 5, 'H': 6, 'K': 7, 'M': 8, 'N': 9, 'R': 10, 'S': 11, 'T': 12, 'V': 13, 'W': 14, 'Y': 15}
    return d

def _baseToInt(character:str, dictBases:dict):
    return dictBases[character]

def _intToBitConversion(intConvBase: int):
    return '{:04b}'.format(intConvBase)

def _byteToIntConversion(bits:str):
    result = 0
    for bit in bits:
        result = (result << 1) | int(bit)
    return result

def _mergeBitListToByteList(bitList):
    bitList = iter(bitList)
    return [bits+next(bitList, '') for bits in bitList]

def binCompress(sequence:str = "ATCG"):
    bitList = []
    dictBases = _baseToIntDict()
    for character in sequence:
        intBase = _baseToInt(character, dictBases)
        bitList.append(_intToBitConversion(intBase))
    if (len(bitList) % 2) > 0: # Add padding if necessary with a gap.
        bitList.append(_bitConversion(0))
    # Each 2 items in bitList forms a byte.
    byteList = _mergeBitListToByteList(bitList)
    byteList = [_byteToIntConversion(byte) for byte in byteList]
    return byteList


def countCompress(sequence:str = "ATCG"):
    seqList = []
    dictBases = _baseToIntDict()
    prevChar = sequence[0]
    count = 0 
    for character in sequence:
        if prevChar == character:
            count += 1
        else:
            seqList.append(str(count))
            seqList.append(prevChar)
            prevChar = character
            count = 1
    # Make sure last bases are written
    seqList.append(str(count))
    seqList.append(prevChar)
    # Each 2 items in seqList forms a pair. First item is the base, and second item is the count.
    return seqList


def binCountCompress(sequence:str = "ATCG"):
    bitList = []
    dictBases = _baseToIntDict()
    prevChar = sequence[0]
    count = 0 
    for character in sequence:
        if prevChar == character and count < 17: # max of 16 to work with bits.
            count += 1
        else:
            intBase = _baseToInt(prevChar, dictBases)
            bitList.append(_intToBitConversion(count-1))
            bitList.append(_intToBitConversion(intBase))
            prevChar = character
            count = 1
    # Make sure last bases are written
    intBase = _baseToInt(prevChar, dictBases)
    bitList.append(_intToBitConversion(count-1))
    bitList.append(_intToBitConversion(intBase))
    # Each 2 items in bitList form a byte. First item is the base, and second item is the count.
    byteList = _mergeBitListToByteList(bitList)
    byteList = [_byteToIntConversion(byte) for byte in byteList]
    return byteList 
