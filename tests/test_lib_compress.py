import pytest

from BioStringCompress import lib_compress

d_out = {'-': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'G': 5, 'H': 6, 'K': 7, 'M': 8, 'N': 9, 'R': 10, 'S': 11, 'T': 12, 'V': 13, 'W': 14, 'Y': 15}

def test__baseToIntDict():
    assert d_out == lib_compress._baseToIntDict()

def test__baseToInt_gap():
    assert 0 == lib_compress._baseToInt("-", d_out)

def test__baseToInt_A():
    assert 1 == lib_compress._baseToInt("A", d_out)

def test__baseToInt_B():
    assert 2 == lib_compress._baseToInt("B", d_out)

def test__baseToInt_C():
    assert 3 == lib_compress._baseToInt("C", d_out)

def test__baseToInt_D():
    assert 4 == lib_compress._baseToInt("D", d_out)

def test__baseToInt_G():
    assert 5 == lib_compress._baseToInt("G", d_out)

def test__baseToInt_H():
    assert 6 == lib_compress._baseToInt("H", d_out)

def test__baseToInt_K():
    assert 7 == lib_compress._baseToInt("K", d_out)

def test__baseToInt_M():
    assert 8 == lib_compress._baseToInt("M", d_out)

def test__baseToInt_N():
    assert 9 == lib_compress._baseToInt("N", d_out)

def test__baseToInt_R():
    assert 10 == lib_compress._baseToInt("R", d_out)

def test__baseToInt_S():
    assert 11 == lib_compress._baseToInt("S", d_out)

def test__baseToInt_T():
    assert 12 == lib_compress._baseToInt("T", d_out)

def test__baseToInt_V():
    assert 13 == lib_compress._baseToInt("V", d_out)

def test__baseToInt_W():
    assert 14 == lib_compress._baseToInt("W", d_out)

def test__baseToInt_Y():
    assert 15 == lib_compress._baseToInt("Y", d_out)

def test__intToBitConversion():
    assert '0000' == lib_compress._intToBitConversion(0)

def test__byteToIntConversion():
    assert 0 == lib_compress._byteToIntConversion('00000000')

def test__mergeBitListToByteList():
    assert ['00000001'] == lib_compress._mergeBitListToByteList(['0000', '0001'])

def test_binCompress():
    assert [28, 53] == lib_compress.binCompress()

def test_countCompress():
    assert ['1', 'A', '1', 'T', '1', 'C', '1', 'G'] == lib_compress.countCompress()

def test_binCountCompress():
    assert [1, 12, 3, 5] == lib_compress.binCountCompress()