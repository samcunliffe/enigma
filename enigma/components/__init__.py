"""Components of the Enigma machine.

Classes and definitions of the Enigma machine components (plugboard, rotors,
and reflectors).
"""


from .reflector import Reflector
from .rotor import Rotor
from .plugboard import Plugboard

# Rotors and reflectors for the Enigma I M3 Army-type.
#
# https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
# .. and ..
# https://en.wikipedia.org/wiki/Enigma_rotor_details#Turnover_notch_positions
ukwb = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT", "UKW-B")
ukwc = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL", "UKW-C")
ukwd = Reflector("ZYXWVUTSRQPONMLKJIHGFEDCBA", "UKW-D")

r1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", starting="A", name="I")
r2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", starting="A", name="II")
r3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", starting="A", name="III")
r4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J", starting="A", name="IV")
r5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z", starting="A", name="V")

# An example plugboard configuration
plugboard_eg = Plugboard("EJ OY IV AQ KW FX MT PS LU BD")
