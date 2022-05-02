import warnings




class Plugboard:
    """A plugboard for a military-grade Enigma machine.

    A simple bidirectional mapping between pairs of characters.
    """

    def __init__(self, list_of_pairs=""):
        self.mapping = self._to_dictionary(list_of_pairs)
        self.name = list_of_pairs

    def __str__(self):
        return self.name

    def __call__(self, c):
        if c in self.mapping.keys():
            return self.mapping[c]
        else:
            return c

    def _to_dictionary(self, list_of_pairs):
        """Convert to a python dictionary and check the input form"""
        li = list_of_pairs.split()
    
        # can only have a max of 13 cables connecting pairs of 26 letters
        if len(li) > 13:
            raise ValueError("Invalid plugboard configuration:", list_of_pairs)
    
        # normally only use 10 cables
        if len(li) > 10:
            warnings.warn("You have more than 10 cables in the plugboard")
    
        # check every pair is really a pair of letters (check unphysical wiring)
        if any([len(pair) !=2 for pair in li]):
            raise ValueError("Invalid plugboard configuration:", list_of_pairs)
    
        # add reversed list (for the inverse mapping) and create dictonary
        li += [el[::-1] for el in li]
        return {key: val for key, val in li}
    
    
