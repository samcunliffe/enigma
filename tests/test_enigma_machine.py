import unittest
import enigma.components as components
from enigma.machine import EnigmaMachine


class TestEnigmaMachineNoPlugboard(unittest.TestCase):
    """Tests of encoding and decoding with three rotors [ I II III ], the UKW-B
    reflector and no plugboard"""

    def setUp(self):
        """Create the test Enigma machine"""
        self.enigma = EnigmaMachine(
            components.ukwb, [components.r1, components.r2, components.r3], None
        )

    def tearDown(self):
        self.enigma.reset()

    def test_rotor_notches_advancement(self):
        """Test that the notches correctly advance neighbouring rotors"""

        for i in range(130):

            # First easy check that the fast rotor is working in the machine.
            self.assertEqual(self.enigma.fast_rotor.start, i % 26)

            # The test machine is set up as [ I II III ] with notches at
            # positions [ Q E V ] which are integer poisitons [ 16 4 21 ]. The
            # fast rotor notch should engage when the rotation count goes
            # 21-->22  (and +26), and advance the middle rotor...
            if i <= 21:
                self.assertEqual(self.enigma.midl_rotor.start, 0)
            if i > 21 and i <= 47:  # (47 = 21 + 26)
                self.assertEqual(self.enigma.midl_rotor.start, 1)
            if i == 48:
                self.assertEqual(self.enigma.midl_rotor.start, 2)

            # ... likewise when the middle rotor notch (at 4) engages, the
            # rotation count should be 125 = 21+(4*26). The middle rotor must
            # advance the slow rotor
            if i < 125:
                self.assertEqual(self.enigma.slow_rotor.start, 0)
            if i == 126:
                self.assertEqual(self.enigma.slow_rotor.start, 1)

            # here is the actual rotation call
            self.enigma._rotate()

    def test_never_map_to_self(self):
        """A character can never map to itself"""
        ciphertext = self.enigma(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        )
        self.assertNotIn("A", ciphertext)

    def test_reset(self):
        """Encoding the same word twice should produce the same ciphertext"""
        first = self.enigma("TURING")
        self.assertEqual(first, self.enigma("TURING"))

        first = self.enigma("WETTERBERICHT")
        self.assertEqual(first, self.enigma("WETTERBERICHT"))

    def test_in_out_character(self):
        """Check we can encode and decode one character"""
        self.assertEqual(self.enigma(self.enigma("A")), "A")
        self.assertEqual(self.enigma(self.enigma("B")), "B")

    def test_in_out_word(self):
        """Check we can encode and decode a word"""
        self.assertEqual(self.enigma(self.enigma("TURING")), "TURING")
        self.assertEqual(self.enigma(self.enigma("WETTERBERICHT")), "WETTERBERICHT")

    def test_in_out_long_message(self):
        """Check we can encode and decode a rather long message"""

        long_message = """
        The Imitation Game 

        I PROPOSE to consider the question, ‘Can machines think?’ This should
        begin with definitions of the meaning of the terms ‘machine’ and
        ‘think’. The definitions might be framed so as to reflect so far as
        possible the normal use of the words, but this attitude is dangerous.
        If the meaning of the words ‘machine’ and ‘think’ are to be found by
        examining how they are commonly used it is difficult to escape the
        conclusion that the meaning and the answer to the question, ‘Can
        machines think?’ is to be sought in a statistical survey such as a
        Gallup poll. But this is absurd. Instead of attempting such a
        definition I shall replace the question by another, which is closely
        related to it and is expressed in relatively unambiguous words.
        """

        # need to convert to upper and remove all spaces, punctiuation etc.
        long_message = "".join(filter(str.isalpha, long_message)).upper()

        self.assertEqual(long_message, self.enigma(self.enigma(long_message)))


if __name__ == "__main__":
    unittest.main()
