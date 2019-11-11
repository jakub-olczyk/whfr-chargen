"""
Dice class for easier creation of generators based on the descriptions in books

>>> print(Dice('d100'))
Dice('d100')

>>> 1 <= Dice('d100').throw() <= 100
True

>>> Dice('d1').throw() == 1
True

>>> Dice('2d1').throw() == 2
True

>>> 2 <= Dice('2d10').throw() <= 20
True
"""

class Dice:

    def __init__(self,desc):
        self.desc = desc
        self.generator = self.init(desc)

    def init(self, desc):
        '''
        desc: string - might be '2d10', 'd6', 'd8', 'd100', 'k10'
        '''
        import re
        pattern = re.compile(r'^(\d*)[dk](\d+)$')
        m = pattern.match(desc)
        n_dice, n_sides = m.groups()

        if not n_dice:
            n_dice = 1
        n_dice, n_sides = int(n_dice), int(n_sides)

        def make_generator(n_dice=0, n_sides=6):
            import random
            def gen():
                result = 0
                for d in range(1,n_dice+1):
                    result += random.randint(1,n_sides)
                return result
            return gen
        return make_generator(n_dice,n_sides)

    def __repr__(self):
        return "Dice('" + self.desc + "')"

    def throw(self):
        return self.generator()

