"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0 ):
        """Make a new generator starting at start. Also creates next value """
        self.start = self.next =  start
    
    def __repr__(self):
        """Returns string describing instance  """
        return f'< SerialGenerator start={self.start} next={self.next} >'

    def generate(self):
        """Returns next serial value. """
        self.next += 1
        return self.next  -1

    def reset(self):
        """Restarts serial number back to starting value """
        self.next = self.start
        return self.next


