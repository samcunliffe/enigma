import unittest
import enigma.components as components
from enigma.machine import EnigmaMachine


class TestEnigmaMachine(unittest.TestCase):
    """Tests of encoding and decoding with three rotors [ I II III ], the UKW-B
    reflector and varying other configurations"""

    def setUp(self):
        """Create the test Enigma machines"""
        self.enigma_simple = EnigmaMachine(
            components.ukwb,
            [components.r1, components.r2, components.r3],
        )
        self.enigma_offsets = EnigmaMachine(
            components.ukwb, [components.r1, components.r2, components.r3], "DEF"
        )
        self.enigma_plugboard = EnigmaMachine(
            components.ukwb,
            [components.r1, components.r2, components.r3],
            plugboard=components.plugboard_eg,
        )

    def tearDown(self):
        self.enigma_simple.clear()
        self.enigma_offsets.clear()
        self.enigma_plugboard.clear()

    def test_rotor_notches_advancement(self):
        """Test that the notches correctly advance neighbouring rotors"""

        for i in range(130):

            # First easy check that the fast rotor is working in the machine.
            self.assertEqual(self.enigma_simple.fast_rotor.current_position, i % 26)

            # The test machine is set up as [ I II III ] with notches at
            # positions [ Q E V ] which are integer poisitons [ 16 4 21 ]. The
            # fast rotor notch should engage when the rotation count goes
            # 21-->22  (and +26), and advance the middle rotor...
            if i <= 21:
                self.assertEqual(self.enigma_simple.midl_rotor.current_position, 0)
            if i > 21 and i <= 47:  # (47 = 21 + 26)
                self.assertEqual(self.enigma_simple.midl_rotor.current_position, 1)
            if i == 48:
                self.assertEqual(self.enigma_simple.midl_rotor.current_position, 2)

            # ... likewise when the middle rotor notch (at 4) engages, the
            # rotation count should be 125 = 21+(4*26). The middle rotor must
            # advance the slow rotor
            if i < 125:
                self.assertEqual(self.enigma_simple.slow_rotor.current_position, 0)
            if i == 126:
                self.assertEqual(self.enigma_simple.slow_rotor.current_position, 1)

            # here is the actual rotation call
            self.enigma_simple._rotate()

    def test_never_map_to_self(self):
        """A character can never map to itself"""
        ciphertext = self.enigma_simple(
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        )
        self.assertNotIn("A", ciphertext)

    def test_reset(self):
        """Encoding the same word twice should produce the same ciphertext"""
        first = self.enigma_simple("TURING")
        self.assertEqual(first, self.enigma_simple("TURING"))

        first = self.enigma_simple("WETTERBERICHT")
        self.assertEqual(first, self.enigma_simple("WETTERBERICHT"))

    def test_in_out_character_simple(self):
        """Check we can encode and decode one character"""
        self.assertEqual(self.enigma_simple(self.enigma_simple("A")), "A")
        self.assertEqual(self.enigma_simple(self.enigma_simple("B")), "B")

    def test_in_out_word_simple(self):
        """Check we can encode and decode a word"""
        self.assertEqual(self.enigma_simple(self.enigma_simple("TURING")), "TURING")
        self.assertEqual(
            self.enigma_simple(self.enigma_simple("WETTERBERICHT")), "WETTERBERICHT"
        )

    def test_in_out_character_offsets(self):
        """Check we can encode and decode one character"""
        self.assertEqual(self.enigma_offsets(self.enigma_offsets("A")), "A")
        self.assertEqual(self.enigma_offsets(self.enigma_offsets("B")), "B")

    def test_in_out_word_offsets(self):
        """Check we can encode and decode a word"""
        self.assertEqual(self.enigma_offsets(self.enigma_offsets("TURING")), "TURING")
        self.assertEqual(
            self.enigma_offsets(self.enigma_offsets("WETTERBERICHT")), "WETTERBERICHT"
        )

    def test_in_out_character_plugboard(self):
        """Check we can encode and decode one character"""
        self.assertEqual(self.enigma_plugboard(self.enigma_plugboard("A")), "A")
        self.assertEqual(self.enigma_plugboard(self.enigma_plugboard("B")), "B")

    def test_in_out_word_plugboard(self):
        """Check we can encode and decode a word"""
        self.assertEqual(self.enigma_plugboard(self.enigma_plugboard("TURING")), "TURING")
        self.assertEqual(
            self.enigma_plugboard(self.enigma_plugboard("WETTERBERICHT")), "WETTERBERICHT"
        )

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

    def test_in_out_long_message_simple(self):
        """Check we can encode and decode a rather long message"""
        # need to convert to upper and remove all spaces, punctiuation etc.
        long_message = "".join(filter(str.isalpha, self.long_message)).upper()
        self.assertEqual(
            long_message, self.enigma_simple(self.enigma_simple(long_message))
        )

    def test_in_out_long_message_offsets(self):
        """Check we can encode and decode a rather long message"""
        long_message = "".join(filter(str.isalpha, self.long_message)).upper()
        self.assertEqual(
            long_message, self.enigma_offsets(self.enigma_offsets(long_message))
        )

    def test_in_out_long_message_plugboard(self):
        """Check we can encode and decode a rather long message"""
        long_message = "".join(filter(str.isalpha, self.long_message)).upper()
        self.assertEqual(
            long_message, self.enigma_plugboard(self.enigma_plugboard(long_message))
        )


if __name__ == "__main__":
    unittest.main()
