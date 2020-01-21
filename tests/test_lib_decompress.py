import pytest

from BioStringCompress import lib_decompress

d_out = {0: '-', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'G', 6: 'H', 7: 'K', 8: 'M', 9: 'N', 10: 'R', 11: 'S', 12: 'T', 13: 'V', 14: 'W', 15: 'Y'}

def test__intToBaseDict():
    assert d_out == lib_decompress._intToBaseDict()

def test__intToBase_gap():
    assert "-" == lib_decompress._intToBase(0, d_out)

def test__intToBase_A():
    assert "A" == lib_decompress._intToBase(1, d_out)

def test__intToBase_B():
    assert "B" == lib_decompress._intToBase(2, d_out)

def test__intToBase_C():
    assert "C" == lib_decompress._intToBase(3, d_out)

def test__intToBase_D():
    assert "D" == lib_decompress._intToBase(4, d_out)

def test__intToBase_G():
    assert "G" == lib_decompress._intToBase(5, d_out)

def test__intToBase_H():
    assert "H" == lib_decompress._intToBase(6, d_out)

def test__intToBase_K():
    assert "K" == lib_decompress._intToBase(7, d_out)

def test__intToBase_M():
    assert "M" == lib_decompress._intToBase(8, d_out)

def test__intToBase_N():
    assert "N" == lib_decompress._intToBase(9, d_out)

def test__intToBase_R():
    assert "R" == lib_decompress._intToBase(10, d_out)

def test__intToBase_S():
    assert "S" == lib_decompress._intToBase(11, d_out)

def test__intToBase_T():
    assert "T" == lib_decompress._intToBase(12, d_out)

def test__intToBase_V():
    assert "V" == lib_decompress._intToBase(13, d_out)

def test__intToBase_W():
    assert "W" == lib_decompress._intToBase(14, d_out)

def test__intToBase_Y():
    assert "Y" == lib_decompress._intToBase(15, d_out)

def test__intToBitConversion():
    assert '00000000' == lib_decompress._intToBitConversion(0)

def test_binDecompress():
    assert ["A", "T", "C", "G"] == lib_decompress.binDecompress()

def test_countDecompress():
    assert ["A", "T", "C", "G"] == lib_decompress.countDecompress()

def test_binCountDecompress():
    assert ["A", "T", "C", "G"] == lib_decompress.binCountDecompress()