import enigma
import enigma.machine
import enigma.components

# construct a machine with random configuration
random_enigma = enigma.random_configuration()
print(random_enigma)

# encipher and decipher
ciphertext = random_enigma.encipher("SECRETMESSAGE")
print(ciphertext)
deciphered = random_enigma.encipher(ciphertext)
print(deciphered, "\n")

# Construct a machine with some specific configuration
# ----------------------------------------------------
# There are three possible reflectors (UKW-B, C, and D) to choose from,
# five possible rotors (I,.. V) to pick three, and three starting positions.
# Finally, you can connect up to 13 letters together at the plugboard.
my_enigma = enigma.machine.EnigmaMachine(
    enigma.components.ukwb,
    [enigma.components.r1, enigma.components.r2, enigma.components.r3],
    "AAA",
    enigma.components.Plugboard("AB CD EF")
)
print(my_enigma)

# encipher and decipher
ciphertext = my_enigma.encipher("ANOTHERSECRETMESSAGE")
print(ciphertext)
deciphered = my_enigma.encipher(ciphertext)
print(deciphered)
