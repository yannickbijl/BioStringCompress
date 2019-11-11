encoding = {'A': '0000', 'C': '0001', 'G': '0010', 'T': '0011',
            'R': '0100', 'Y': '0101', 'S': '0110', 'W': '0111',
            'K': '1000', 'M': '1001', 'B': '1010', 'D': '1011',
            'H': '1100', 'V': '1101', 'N': '1110', '.': '1111'}

def compress_4bit(sequence: str) -> str:
    binary = []
    for nucleotide in sequence:
        binary.append(encoding.get(nucleotide))
    return "".join(binary)


def compress_5bit(sequence: str) -> str:
    pass


def compress_numeric(sequence: str) -> str:
    seq = []
    prev = None
    count = 0
    for nucleotide in sequence:
        if prev == None or prev != nucleotide:
            seq.append(nucleotide + str(count))
            prev = nucleotide
        else:
            count + 1
    return "".join(seq)