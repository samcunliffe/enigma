from .components import Plugboard


class EnigmaMachine:
    def __init__(self, reflector, rotors, plugboard):
        self.reflector = reflector
        self.slow_rotor, self.midl_rotor, self.fast_rotor = rotors
        if plugboard:
            self.plugboard = plugboard
        else:
            self.plugboard = Plugboard("")  # uncabled --> passthrough

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
                self.fast_rotor.forward(
                    self.midl_rotor.forward(
                        self.slow_rotor.forward(
                            self.reflector(
                                self.slow_rotor.backward(
                                    self.midl_rotor.backward(
                                        self.fast_rotor.backward(self.plugboard(c))
                                    )
                                )
                            )
                        )
                    )
                )
            )
        return encoded

    def decode(self, ciphertext):

        decoded = ""

        for c in ciphertext:

            self._rotate()

            decoded += self.plugboard(
                self.fast_rotor.backward(
                    self.midl_rotor.backward(
                        self.slow_rotor.backward(
                            self.reflector(
                                self.slow_rotor.forward(
                                    self.midl_rotor.forward(
                                        self.fast_rotor.forward(
                                            self.plugboard(c)
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        return decoded

    def reset(self):
        self.slow_rotor.reset()
        self.midl_rotor.reset()
        self.fast_rotor.reset()
