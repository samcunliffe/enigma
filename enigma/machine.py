from .components import Plugboard
from .components.utils import to_letter, to_position


class EnigmaMachine:
    """A type I, M3 or M4 Enigma machine.

    The machine needs to be set up with a reflector, a list of three rotors,
    and an optional plugboard configuration.  Calls to the machine
    encipher/decipher text. Cleartext must be capital letters with no numbers
    or punctiation.

    Attributes:
        reflector (enigma.components.Reflector): the reflector
        slow_rotor (enigma.components.Rotor): the left-most rotor
        midl_rotor (enigma.components.Rotor): the middle rotor
        fast_rotor (enigma.components.Rotor): the right-most rotor
        plugboard (enigma.components.Plugboard): optional plugboard wiring
    """

    def __init__(self, reflector, rotors, starting="AAA", plugboard=None):
        self.reflector = reflector
        self.slow_rotor, self.midl_rotor, self.fast_rotor = rotors

        self.slow_rotor.set_starting(starting[0])
        self.midl_rotor.set_starting(starting[1])
        self.fast_rotor.set_starting(starting[2])

        if plugboard:
            self.plugboard = plugboard
        else:
            # uncabled --> passthrough
            self.plugboard = Plugboard("")

    def __str__(self):
        first = (
            "Enigma machine rotors: "
            + str(self.slow_rotor)
            + " "
            + str(self.midl_rotor)
            + " "
            + str(self.fast_rotor)
        )
        second = " in positions " + self._current_rotation()
        return first + second

    def _rotate(self):
        """Rotates rotors on keypress."""
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
        """A printable string representation of the current rotation"""
        return (
            str(self.slow_rotor.current_position)
            + " "
            + str(self.midl_rotor.current_position)
            + " "
            + str(self.fast_rotor.current_position)
        )

    def __call__(self, message):
        return self.encipher(message)

    def encipher(self, message):
        """Encipher or decipher the ``message``.
        Can also perform this action by calling the EnigmaMachine instance

        Examples:
            >> my_engima("SECRETMESSAGE")
            >> my_enigma.encipher("SECRETMESSAGE")

        Parameters:
            message (str): the message to encipher/decipher must be
                       entirely capitals with no punctuation or numbers etc.

        Returns:
            str: the enciphered or deciphered message

        """
        self.reset()
        output = ""

        for c in message:
            self._rotate()
            #
            # method calls inner to outer:
            #
            #   ╭───────╮    ╭──┬──┬──╮    ╭───────╮
            #   │       │    │  │  │  │    │       │
            #   │ ┌─────│ <- │──│──│──│ <- │───────│ <-- keypress
            #   │ │     │    │  │  │  │    │       │
            #   │ └─────│ -> │──│──│──│ -> │───────│ --> light
            #   │       │    │  │  │  │    │       │
            #   ╰───────╯    ╰──┴──┴──╯    ╰───────╯
            #   reflector    rotors *3     plugboard
            #
            output += self.plugboard(
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
        return output

    def reset(self):
        """Reset all of the rotors to their starting positions"""
        self.slow_rotor.reset()
        self.midl_rotor.reset()
        self.fast_rotor.reset()

    def clear(self):
        """Reset all of the rotors to their "A" positions and forget the offsets"""
        self.slow_rotor.clear()
        self.midl_rotor.clear()
        self.fast_rotor.clear()
