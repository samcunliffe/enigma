import random as _random
import string as _string
from .machine import EnigmaMachine as _EnigmaMachine
from . import components as _components


def random_configuration():
    """Returns an Enigma machine with a random configuration."""
    reflector = _random.choice(
        [_components.ukwb, _components.ukwc, _components.ukwd])
    rotors = _random.choices(
        [_components.r1, _components.r2, _components.r3, _components.r4, _components.r5], k=3)
    _random.shuffle(rotors)
    starting_positions = "".join(_random.choices(_string.ascii_uppercase, k=3))
    mixed_alphabet = _random.sample(_string.ascii_uppercase, 20)
    random_wiring = " ".join(
        [a + b for a, b in zip(mixed_alphabet[:13], mixed_alphabet[13:])]
    )
    plugboard = _components.Plugboard(random_wiring)
    return _EnigmaMachine(reflector, rotors, starting_positions, plugboard)
