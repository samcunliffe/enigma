"""Components of the Enigma machine.

Classes and definitions of the Enigma machine components (plugboard, rotors,
and reflectors).
"""


from .rotor import Rotor
from .plugboard import Plugboard
from .reflector import Reflector


ukwb = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT", "UKW-B")
ukwc = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL", "UKW-C")
ukwd = Reflector("ZYXWVUTSRQPONMLKJIHGFEDCBA", "UKW-D")

r1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", "I")
r2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", "II")
r3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", "III")
r4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J", "IV")
r5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z", "V")
