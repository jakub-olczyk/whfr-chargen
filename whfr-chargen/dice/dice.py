class Dice:

    def __init__(self,desc):
        self.desc = desc
        self.generator = self.init(desc)

    def init(self, desc):
        ''' desc might be 2d10, d6, d8, d100 k10'''
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

    def throw(self):
        return self.generator()

