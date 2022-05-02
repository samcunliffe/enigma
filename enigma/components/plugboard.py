import warnings


def to_dictionary(list_of_pairs):
    """..."""
    li = list_of_pairs.split()
    li += [el[::-1] for el in li]
    return {key: val for key, val in li}


class Plugboard:
    """A plugboard for a military-grade Enigma machine.

    A simple two-directional mapping between pairs of characters.
    """

    def __init__(self, list_of_pairs=""):
        self.mapping = to_dictionary(list_of_pairs)

    def __call__(self, c):
        if c in self.mapping.keys():
            return self.mapping[c]
        else:
            return c
