import numpy as np
import pandas as pd

class Die:
    """
    Roll a die n times.  Number of sides defaults to 6.
    """

    def __init__(self, sides=6, n=None):
        self.sides = sides
        self.results = None
        self.n=n
        if n:
            self.roll(n)


    def roll(self, n):
        self.n = n
        results = np.ceil(np.random.rand(n)*self.sides)
        results = pd.value_counts(pd.Series(results))
        results.sort_index(ascending=True)
        self.results = results

    @property
    def frequency(self):
        if not self.n:
            raise AttributeError('Die has not been rolled')
        return self.results/self.n
