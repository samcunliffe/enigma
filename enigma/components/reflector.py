from .utils import to_position, verify_alphabet


class Reflector:
    """A non-configurable rotor for an Enigma machine.

    A simple wiring from A-Z to a different letter, but does not rotate.
    Therefore much simpler than the `enigma.components.Rotor`.

    Attributes:
        a (str): the mapping in A-Z order
        name (str): an optional name for the reflector

    TODO:
        Verify that the array provided is a valid physical wiring.
    """

    def __init__(self, array, name=None):
        verify_alphabet(array)
        self.a = array

    def __call__(self, c):
        return self.a[to_position(c)]
