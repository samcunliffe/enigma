import string
import enigma.components as _cp


def test_uncabled():
    """Test an uncabled (passthrough) plugboard"""
    plugboard = _cp.Plugboard()
    for ch in string.ascii_uppercase:
        assert plugboard(ch) == ch


def test_one_cable():
    """Test one cabled pair"""
    plugboard = _cp.Plugboard("AB")
    assert plugboard("A") == "B"
    assert plugboard("B") == "A"
    # (uncabled)
    for ch in string.ascii_uppercase[2:]:
        assert plugboard(ch) == ch


def test_ten_cables():
    """Test a reasonable example configuration: 10 cabled pairs"""
    plugboard = _cp.Plugboard("EJ OY IV AQ KW FX MT PS LU BD")
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
