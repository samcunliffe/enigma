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

    def test_never_map_to_self(self):
        """A character can never map to itself"""
        input_string = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        ciphertext = self.enigma.encode(input_string)
        self.assertNotIn("A", ciphertext)

    def test_in_out_1(self):
        """Check we can encode and decode one charachter"""
        assert self.enigma.encode(self.enigma.decode("A")) == "A"
        assert self.enigma.encode(self.enigma.decode("B")) == "B"

    def test_in_out_1(self):
        """Check we can encode and decode a word"""
        assert self.enigma.encode(self.enigma.decode("TURING")) == "TURING"
        assert self.enigma.encode(self.enigma.decode("TURING")) == "TURING"

    def test_encoding(self):
        """Test encoding a sample input"""
        input_string = "WETTERBERICHT"
        expected_cyphertext = "KLHFRTJYDUWON"
        ciphertext = self.enigma.encode(input_string)
        self.assertEqual(expected_cyphertext, ciphertext)

    def test_decoding(self):
        """Test decoding a sample ciphertext"""
        ciphertext = "KLHFRTJYDUWON"
        expected_cleartext = "WETTERBERICHT"
        cleartext = self.enigma.decode(ciphertext)
        self.assertEqual(expected_cleartext, cleartext)


if __name__ == "__main__":
    unittest.main()
