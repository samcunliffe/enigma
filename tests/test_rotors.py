import pytest
import enigma.components as components


def test_invalid_construction():
    """Can't construct with either too many or too few letters"""
    with pytest.raises(ValueError):
        r = components.Rotor("A", "A")
    with pytest.raises(ValueError):
        r = components.Rotor("AABCDEFGHIJKLMNOPQRSTUVWXYZ", "A")


def test_single_rotor_forward():
    """Forward call to rotator I"""
    assert components.r1.forward("A") == "E"
    assert components.r1.forward("B") == "K"
    assert components.r1.forward("C") == "M"
    assert components.r1.forward("D") == "F"

def test_single_rotor_backward():
    """Backward call to rotator I"""
    assert components.r1.backward("E") == "A"
    assert components.r1.backward("K") == "B"
    assert components.r1.backward("M") == "C"
    assert components.r1.backward("F") == "D"


def test_repeated_rotation():
    """Repeated rotations should wrap around"""
    [components.r1.rotate() for i in range(26)]
    assert components.r1.forward("A") == "E"


def test_notch_position():
    """Check that at_notch returns True when we're at the notch."""
    components.r4.reset()

    # rotor IV has a notch at the "J" position (9)
    for i in range(26):
        if i == 9:
            assert components.r4.at_notch() == True
        else:
            assert components.r4.at_notch() == False
        components.r4.rotate()

    
