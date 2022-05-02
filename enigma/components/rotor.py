import string
from .utils import to_position, verify_alphabet


class Rotor:
    """A rotor for an Enigma machine.

    Has a cyclical mapping from each letter A-Z to a different letter, and a
    notch at a given position (which causes the next rotor to rotate).
    """

    def __init__(self, a_position, notch, name=None):
        verify_alphabet(a_position)
        self.a = a_position
        self.n = to_position(notch)
        self.name = name
        self.start = 0
        self._get_inverse_map()

    def __str__(self):
        return self.name if self.name else self.a

    def _get_inverse_map(self):
        """Given the forward wiring in the "A" position, we need to know the
        inverse map (also in the "A" position)."""

        # pair up the map with the alphabet ABC..Z
        list_of_tuples = [(a, b) for a, b in zip(self.a, string.ascii_uppercase)]
        # now reorder based on the alphebetised map (which scrambles ABC...)
        self.b = "".join([second for _, second in sorted(list_of_tuples)])

    def forward(self, c):
        """Current through the rotor in the forward direction"""
        point = self.start + to_position(c)
        return (self.a[point:] + self.a[:point])[0]

    def backward(self, c):
        """Current going backwards through the rotor"""
        point = self.start + to_position(c)
        return (self.b[point:] + self.b[:point])[0]

    def rotate(self):
        """Rotate the rotor"""
        if self.start < 26:
            self.start += 1
        else:
            self.start = 0

    def at_notch(self):
        """Are we at a notch position?
        (the machine may need to rotate other rotors)"""
        return self.start == self.n

    def reset(self):
        self.start = 0
