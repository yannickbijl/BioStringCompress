def charToIntDict():
    allBases = ["A", "C", "G", "T", "R", "Y", "S", "W", "K", "M", "B", "D", 
                "H", "V", "N", "-"]
    d = dict([(y,x) for x,y in enumerate(sorted(set(allBases)))])
    # d = {'-': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'G': 5, 'H': 6, 'K': 7, 'M': 8, 'N': 9, 'R': 10, 'S': 11, 'T': 12, 'V': 13, 'W': 14, 'Y': 15}
    return d

def charToInt(character:str, dictBases:dict):
    return dictBases[character]

def bitConversion(intConvBase: int):
    return '{:04b}'.format(intConvBase)


def binCompress(sequence:str = "ATCG"):
    bitList = []
    dictBases = charToIntDict()
    for character in sequence:
        intBase = charToInt(character, dictBases)
        bitList.append(bitConversion(intBase))
    if (len(bitList) % 2) > 0: # Add padding if necessary with a gap.
        bitList.append(bitConversion(0))
    return bitList # Each 2 items in bitList forms a byte.


def countCompress(sequence:str = "ATCG"):
    seqList = []
    dictBases = strToIntDict()
    prevChar = seq[0]
    count = 0 
    for character in sequence:
        if prevChar == character:
            count += 1
        else:
            seqList.append(prevChar)
            seqList.append(count)
            prevChar = character
            count = 1
    return seqList # Each 2 items in seqList forms a pair. First item is the base, and second item is the count.


def binCountCompress(sequence:str = "ATCG"):
    bitList = []
    dictBases = strToIntDict()
    prevChar = seq[0]
    count = 0 
    for character in sequence:
        if prevChar == character and count < 17: # max of 16 to work with bits.
            count += 1
        else:
            intBase = charToInt(prevChar, dictBases)
            bitList.append(bitConversion(intBase))
            bitList.append(bitConversion(count-1))
            prevChar = character
            count = 1
    return bitList # Each 2 items in bitList form a byte. First item is the base, and second item is the count.
