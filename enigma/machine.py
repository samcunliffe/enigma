from .components import Plugboard


class EnigmaMachine:
    def __init__(self, reflector, rotors, plugboard):
        self.reflector = reflector
        self.slow_rotor, self.midl_rotor, self.fast_rotor = rotors
        if plugboard:
            self.plugboard = plugboard
        else:
            self.plugboard = Plugboard("") # uncabled --> passthrough

    def __str__(self):
        return "Hello"

    def _rotate(self):
        """Rotates rotors after a keypress."""
        if self.fast_rotor.at_notch() and self.midl_rotor.at_notch():
            self.slow_rotor.rotate()
            self.midl_rotor.rotate()
            self.fast_rotor.rotate()

        elif self.fast_rotor.at_notch():
            self.midl_rotor.rotate()
            self.fast_rotor.rotate()

        else:
            self.fast_rotor.rotate()

    def encode(self, message):
        encoded = ""

        for c in message:

            self._rotate()

            encoded += self.plugboard(
                self.fast_rotor(
                    self.midl_rotor(
                        self.slow_rotor(
                            self.reflector(
                                self.slow_rotor(
                                    self.midl_rotor(self.fast_rotor(self.plugboard(c)))
                                )
                            )
                        )
                    )
                )
            )
        return encoded

    def decode(self, ciphertext):
        pass

    def reset(self):
        self.slow_rotor.reset()
        self.midl_rotor.reset()
        self.fast_rotor.reset()
