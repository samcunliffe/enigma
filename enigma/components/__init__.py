"""Components of the Enigma machine.

Classes and definitions of the Enigma machine components (plugboard, rotors,
and reflectors).
"""


from .reflector import Reflector
from .rotor import Rotor
from .plugboard import Plugboard


ukwb = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT", "UKW-B")
ukwc = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL", "UKW-C")
ukwd = Reflector("ZYXWVUTSRQPONMLKJIHGFEDCBA", "UKW-D")

# Rotors for the Enigma I M3 Army-type.
#
# https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
# .. and ..
# https://en.wikipedia.org/wiki/Enigma_rotor_details#Turnover_notch_positions
r1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", "I")
r2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", "II")
r3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", "III")
r4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J", "IV")
r5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z", "V")


# An example plugboard configuration
plugboard_eg = Plugboard("EJ OY IV AQ KW FX MT PS LU BD")
