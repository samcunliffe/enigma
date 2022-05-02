from .components import Plugboard
from .components.utils import to_letter


class EnigmaMachine:
    def __init__(self, reflector, rotors, plugboard):
        self.reflector = reflector
        self.slow_rotor, self.midl_rotor, self.fast_rotor = rotors
        if plugboard:
            self.plugboard = plugboard
        else:
            self.plugboard = Plugboard("")  # uncabled --> passthrough

    def __str__(self):
        first = "Enigma machine rotors: " + str(self.slow_rotor) + " " + str(self.midl_rotor) + " " + str(self.fast_rotor)
        second = " in positions " + self._current_rotation()
        return first + second

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

    def _current_rotation(self):
        return str(self.slow_rotor.start) + " " + str(self.midl_rotor.start) + " " + str(self.fast_rotor.start)

    def encode(self, message):

        self.reset()
        #print(self)
        encoded = ""

        for c in message:

            self._rotate()
            print(self)

            encoded += self.plugboard(
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
        return encoded

    def reset(self):
        self.slow_rotor.reset()
        self.midl_rotor.reset()
        self.fast_rotor.reset()
