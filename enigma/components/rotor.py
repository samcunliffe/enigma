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

    def __str__(self):
        return self.name if self.name else self.a

    def __call__(self, c):
        point = self.start + to_position(c)
        return (self.a[point:] + self.a[:point])[0]

    def rotate(self):
        if self.start < 26:
            self.start += 1
        else:
            self.start = 0

    def at_notch(self):
        return self.start == self.n

    def reset(self):
        self.start = 0

    def setup(self, starting_position):
        raise NotImplementedError()
