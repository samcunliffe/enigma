import enigma.components.utils as _utils


def test_to_letter():
    assert _utils.to_letter(0) == "A"
    assert _utils.to_letter(25) == "Z"


def test_to_position():
    assert _utils.to_position("A") == 0
    assert _utils.to_position("Z") == 25
