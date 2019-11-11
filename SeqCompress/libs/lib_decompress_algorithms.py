encoding = {'0000': 'A', '0001': 'C', '0010': 'G', '0011': 'T',
            '0100': 'R', '0101': 'Y', '0110': 'S', '0111': 'W',
            '1000': 'K', '1001': 'M', '1010': 'B', '1011': 'D',
            '1100': 'H', '1101': 'V', '1110': 'N', '1111': '.'}

def decompress_4bit(binary: str) -> str:
    sequence = []
    binary = [binary[i:i+4] for i in range(0, len(binary), 4)] # transform into list with strings of length 4.
    for bincode in binary:
        sequence.append(encoding.get(bincode))
    return "".join(sequence)

def decompress_5bit(binary: str) -> str:
    pass


def decompress_numeric(sequence: str) -> str:
    pass