import pytest
import os

from BioStringCompress import lib_data

def test_translatRNAToDNA():
    assert ['A', 'T', 'T', 'C', 'G'] == lib_data.translateDNAToRNA(['A', 'U', 'U', 'C', 'G'])

def test_translateDNAToRNA():
    assert ['A', 'U', 'U', 'C', 'G'] == lib_data.translateDNAToRNA(['A', 'T', 'T', 'C', 'G'])

def test__checkPathdirExist_Success(tmp_path):
    d = tmp_path / "sub"
    p = d / "simple.txt"
    lib_data._checkPathdirExist(p, create=True)
    assert True == os.path.isdir(d)

def test__checkPathdirExist_Failure(tmp_path):
    d = tmp_path / "sub"
    p = d / "simple.txt"
    with pytest.raises(FileNotFoundError):
        lib_data._checkPathdirExist(p)

def test_readBinary(tmpdir):
    p = tmpdir.join("simple.txt")
    p.write(bytes([28, 53]))
    assert [28, 53] == lib_data.readBinary(p)

def test_readNormal_Uncompressed(tmpdir):
    p = tmpdir.join("simple.txt")
    p.write("ATCG")
    assert ["A", "T", "C", "G"] == lib_data.readNormal(p)

def test_readNormal_Compressed(tmpdir):
    p = tmpdir.join("simple.txt")
    p.write("1A1T1C1G")
    assert ["1A", "1T", "1C", "1G"] == lib_data.readNormal(p)

def test_writeBinary(tmpdir):
    # Trust only if 'test_readBinary' passed
    p = tmpdir.join("simple.txt")
    lib_data.writeBinary(p, [1, 12, 3, 5])
    assert [1, 12, 3, 5] == lib_data.readBinary(p)

def test_writeNormal(tmpdir):
    p = tmpdir.join("simple.txt")
    lib_data.writeNormal(p, ["1", "A", "1", "T", "1", "C", "1","G"])
    assert "1A1T1C1G" == p.read()