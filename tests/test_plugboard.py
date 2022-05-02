<<<<<<< HEAD
import pytest
import string
import enigma.components as components


def test_invalid_construction_1():
    """Can't have a valid plugboard configuration with more than 13 cables"""
    with pytest.raises(ValueError):
        p = components.Plugboard("AB CD EF GH IJ KL MN OP QR ST UV WX YZ AZ")


def test_invalid_construction_2():
    """Can't have a valid plugboard with a cable connecting three letters"""
    with pytest.raises(ValueError):
        p = components.Plugboard("ABC DE")
    with pytest.raises(ValueError):
        p = components.Plugboard("AB CDE")
    with pytest.raises(ValueError):
        p = components.Plugboard("AB CDE FG")


def test_invalid_construction_3():
    """Can't have a valid plugboard with a cable connecting to nothing"""
    with pytest.raises(ValueError):
        p = components.Plugboard("A")
    with pytest.raises(ValueError):
        p = components.Plugboard("A BC DE")
    with pytest.raises(ValueError):
        p = components.Plugboard("AB C DE")
=======
import string
import enigma.components as _cp
>>>>>>> 3c32e85519ab2546ce67a1a42a45c2684aff8b4a


def test_uncabled():
    """Test an uncabled (passthrough) plugboard"""
<<<<<<< HEAD
    plugboard = components.Plugboard()
=======
    plugboard = _cp.Plugboard()
>>>>>>> 3c32e85519ab2546ce67a1a42a45c2684aff8b4a
    for ch in string.ascii_uppercase:
        assert plugboard(ch) == ch


def test_one_cable():
    """Test one cabled pair"""
<<<<<<< HEAD
    plugboard = components.Plugboard("AB")
=======
    plugboard = _cp.Plugboard("AB")
>>>>>>> 3c32e85519ab2546ce67a1a42a45c2684aff8b4a
    assert plugboard("A") == "B"
    assert plugboard("B") == "A"
    # (uncabled)
    for ch in string.ascii_uppercase[2:]:
        assert plugboard(ch) == ch


def test_ten_cables():
    """Test a reasonable example configuration: 10 cabled pairs"""
<<<<<<< HEAD
    plugboard = components.Plugboard("EJ OY IV AQ KW FX MT PS LU BD")
=======
    plugboard = _cp.Plugboard("EJ OY IV AQ KW FX MT PS LU BD")
>>>>>>> 3c32e85519ab2546ce67a1a42a45c2684aff8b4a
    assert plugboard("E") == "J"
    assert plugboard("J") == "E"
    assert plugboard("O") == "Y"
    assert plugboard("Y") == "O"
    assert plugboard("I") == "V"
    assert plugboard("V") == "I"
    assert plugboard("A") == "Q"
    assert plugboard("Q") == "A"
    assert plugboard("K") == "W"
    assert plugboard("W") == "K"
    assert plugboard("F") == "X"
    assert plugboard("X") == "F"
    assert plugboard("M") == "T"
    assert plugboard("T") == "M"
    assert plugboard("P") == "S"
    assert plugboard("S") == "P"
    assert plugboard("L") == "U"
    assert plugboard("U") == "L"
    assert plugboard("B") == "D"
    assert plugboard("D") == "B"
    # (uncabled)
    assert plugboard("C") == "C"
    assert plugboard("G") == "G"
    assert plugboard("H") == "H"
    assert plugboard("N") == "N"
    assert plugboard("R") == "R"
    assert plugboard("Z") == "Z"
