import unittest
import enigma.components as _cp
import enigma.machine as _em


class TestEnigmaMachineNoPlugboard(unittest.TestCase):
    """Tests of encoding and decoding with three rotors and no plugboard"""

    def setUp(self):
        """Create the test Enigma machine"""
        self.enigma = _em.EnigmaMachine(_cp.ukwb, [_cp.r1, _cp.r2, _cp.r3], None)

    def tearDown(self):
        self.enigma.reset()

    def test_rotor_notches_advancement(self):
        """Test that the notches correctly advance neighbouring rotors"""

        for i in range(200):


            # First easy check that the fast rotor is working in the machine.
            self.assertEqual(self.enigma.fast_rotor.start, i % 27)

            # The test machine is set up as [ I II III ] with notches at
            # positions [ Q E V ] which are integer poisitons [ 16 4 21 ]. The
            # fast rotor at positions 21, 42, (etc) must advance the middle
            # rotor...
            #if i < 21:
            #   self.assertEqual(self.enigma.midl_rotor.start, 0)
            #if i >= 21 and i < 42:
            #   self.assertEqual(self.enigma.midl_rotor.start, 1)
            #if i == 42:
            #   self.assertEqual(self.enigma.midl_rotor.start, 2)

            ## ... likewise when we get to 21*4 = 84, the middle rotor must
            ## advance the slow rotor
            # if i < 84:
            #    self.assertEqual(self.enigma.slow_rotor.start, 0)
            # if i == 84:
            #    self.assertEqual(self.enigma.slow_rotor.start, 1)

            if i == 199:
                self.assertEqual(0, 1)

            self.enigma._rotate()
            print(i, " ", self.enigma._current_rotation())

    def test_never_map_to_self(self):
        """A character can never map to itself"""
        input_string = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        ciphertext = self.enigma.encode(input_string)
        self.assertNotIn("A", ciphertext)

    def test_reset(self):
        """Encoding the same word twice should produce the same ciphertext"""
        first = self.enigma.encode("TURING")
        self.assertEqual(first, self.enigma.encode("TURING"))

        first = self.enigma.encode("WETTERBERICHT")
        self.assertEqual(first, self.enigma.encode("WETTERBERICHT"))

    def test_in_out_character(self):
        """Check we can encode and decode one character"""
        self.assertEqual(self.enigma.encode(self.enigma.encode("A")), "A")
        self.assertEqual(self.enigma.encode(self.enigma.encode("B")), "B")

    @unittest.skip
    def test_in_out_word(self):
        """Check we can encode and decode a word"""
        self.assertEqual(self.enigma.encode(self.enigma.encode("TURING")), "TURING")
        self.assertEqual(
            self.enigma.encode(self.enigma.encode("WETTERBERICHT")), "WETTERBERICHT"
        )

    @unittest.skip
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

        self.assertEqual(
            long_message, self.enigma.encode(self.enigma.encode(long_message))
        )


if __name__ == "__main__":
    unittest.main()

