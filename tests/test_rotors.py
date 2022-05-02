import pytest
import enigma.components as components


def test_invalid_construction():
    """Can't construct with either too many or too few letters"""
    with pytest.raises(ValueError):
        r = components.Rotor("A", "A")
    with pytest.raises(ValueError):
        r = components.Rotor("AABCDEFGHIJKLMNOPQRSTUVWXYZ", "A")


def test_single_rotor():
    """First call to rotator R1"""
    assert components.r1("A") == "E"


def test_repeated_rotation():
    """Repeated rotations should wrap around"""
    [components.r1.rotate() for i in range(26)]
    assert components.r1("A") == "E"
