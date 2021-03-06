"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'
    
    def __init__(self, name, flavor, price, qty=0):

      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = qty

      self.cache[name] = self

    def add_stock(self, amount):

      self.qty += amount

    def sell(self, amount):

      if self.qty == 0:
        print("Sorry, these cupcakes are sold out")

      elif self.qty < amount:
        self.qty = 0

      else:
        self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount):
      
      new_ingredients = []

      for tupl in ingredients:

        tupl = (tupl[0], tupl[1] * amount)
        new_ingredients.append(tupl)

      return new_ingredients

    @classmethod
    def get(cls, name):

      if name not in cls.cache:
        print("Sorry, that cupcake doesn't exist")

      else:
        return cls.cache[name]

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
