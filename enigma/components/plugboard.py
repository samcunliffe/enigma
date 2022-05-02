import warnings


class Plugboard:
    def __init__(self, list_of_pairs=None, passthrough=True):

        if passthrough and list_of_pairs:
            warnings.warn(
                "Have provided both passthrough=True, and a plugboard configuration. Will ignore the latter."
            )

        if passthrough:
            self.passthrough = True
            self.list_of_pairs = None
        else:
            self.passthrough = False
            self.list_of_pairs = list_of_pairs

    def __call__(self, c):
        if self.passthrough:
            return c
        else:
            raise NotImplementedError("Plugboard not implemented yet")
