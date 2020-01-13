def strToIntDict(allBases):
    #d = {'-': 1, 'A': 2, 'B': 3, 'C': 4, 'D': 5, 'G': 6, 'K': 7, 'M': 8, 
    #     'N': 9, 'R': 10, 'S': 11, 'T': 12, 'V': 13, 'W': 14, 'Y': 15}
    d = dict([(y,x+1) for x,y in enumerate(sorted(set(allBases)))])
    return(d)

def strToInt(sequenceBase, dictBases):
    sequenceInt = []
    for key in list(dictBases.keys()): 
        for base in sequenceBase:
            if base == key:
                sequenceInt.append(dictBases[key])
    return(sequenceInt)

def bitConversion(intConvBase):
    bitBase = '{:04b}'.format(intConvBase)
    return(bitBase)
    
def method1(): # Previously defa
    allBases = ["A", "C", "G", "T", "R", "Y", "S", "W", "K", "M", "B", "D", 
                "H", "V", "N", "-"]
    dictBases = strToIntDict(allBases)
    #print(dictBases)
    sequenceBases = "ACTG" # dummy sequence
    #print(strToInt(sequenceBases, dictBases))



def b():
    return 1


def c():
    return 1
