"""Word Finder: finds random words from a dictionary."""
import random
class WordFinder:
    """ This class will pull words from a file and relay information about that file

    >>> wd = WordFinder(words.txt)
    235886 words read

    >>> wd.random_word(s)
    'roue'
    """

    def __init__(self, path):
        """Opens file and strips away spaces on any words. Shows total num of words """
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):  
        """Removes any space around the word"""
        return [w.strip() for w in file]
    
    def random_word(self):
        """Selects a random word from the file given"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Handles special word cases"""

    def parse(self,file):
        """Parse file, puts words into list. Skips words that start with # """
        return [w.strip() for w in file if w.strip() and not w.startswith("#")]

    
