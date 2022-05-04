import string
from .utils import to_letter, to_position, verify_alphabet


class Rotor:
    """A rotor for an Enigma machine.

    Has a cyclical mapping from each letter A-Z to a different letter, and a
    notch at a given position (which causes the next rotor to rotate).

    Attributes:
        a (str): the mapping in A-Z order in the "A" position
        n (int): the integer position of the notch
        name (str): an optional name for the rotor
        current_position (int): the current rotation offset for the letter A
        start (int): the starting setting offset
    """

    def __init__(self, a_position, notch, starting="A", name=None):
        verify_alphabet(a_position)
        self.a = a_position
        self.n = to_position(notch)
        self.name = name
        self.start = to_position(starting)
        self.current_position = self.start

    def __str__(self):
        return self.name if self.name else self.a

    def forward(self, c):
        """Current through the rotor in the forward direction"""
        return (self.a[self.current_position :] + self.a[: self.current_position])[
            to_position(c)
        ]

    def backward(self, c):
        """Current going backwards through the rotor"""
        return to_letter(
            (self.a[self.current_position :] + self.a[: self.current_position]).find(c)
        )

    def rotate(self):
        """Rotate the rotor"""
        if self.current_position == 25:
            self.current_position = 0
        else:
            self.current_position += 1

    def at_notch(self):
        """Are we at the notch position?
        (the machine may need to rotate other rotors)"""
        return self.current_position == self.n

    def reset(self):
        """Move the rotor back to the starting position"""
        self.current_position = self.start

    def clear(self):
        """Move the rotor back to the "A" position and forget the offset"""
        self.start = 0
        self.reset()
