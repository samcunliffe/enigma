from .utils import to_position, verify_alphabet


class Reflector:
    def __init__(self, array, name=None):
        verify_alphabet(array)
        self.a = array

    def __call__(self, c):
        return self.a[to_position(c)]
