import pytest
import string
import enigma.components as components

def test_invalid_construction():
    """Can't construct with either too many or too few letters"""
    with pytest.raises(ValueError):
        r = components.Reflector("A", "A")
    with pytest.raises(ValueError):
        r = components.Reflector("AABCDEFGHIJKLMNOPQRSTUVWXYZ", "A")


def test_ukwb_reflector():
    """Test a reflector wiring as the UKW-B reflector"""
    ukwb_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    reflector = components.Reflector(ukwb_wiring)
    for a, b in zip(string.ascii_uppercase, ukwb_wiring):
        assert reflector(a) == b

def test_selfwired_reflector():
    """Test a dummy reflector that is wired in passthrough"""
    reflector = components.Reflector(string.ascii_uppercase)
    for c in string.ascii_uppercase:
        assert reflector(c) == c

