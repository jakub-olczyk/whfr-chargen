FULL_NAME_EN = {
        'ws': 'Weapon Skill', 'bs': 'Ballistic Skill', 's': 'Strength',
        't': 'Toughness', 'ag': 'Agility', 'int': 'Intelligence', 'wp':
        'Will Power', 'fel': 'Fellowship', 'a': 'Attacks', 'w':
        'Wounds', 'sb': 'Strength Bonus', 'tb': 'Toughness Bonus', 'm':
        'Movement', 'mag': 'Magic', 'ip': 'Insanity Points', 'fp':
        'Fate Points',
        }
# TODO
FULL_NAME_PL = {}

ORDER = """ws bs s t ag int wp fel""".split()
ORDER2 = """a w sb tb m mag ip fp""".split()
class Characteristics:

    def __init__(self):
        self.stats_plus_2d10 = """ws bs s t ag int wp fel""".split()
        self.recipies = {
                # negative number means recomputing using special rules
                'human_base': {
                    'ws': 20,
                    'bs': 20,
                    's': 20,
                    't': 20,
                    'ag': 20,
                    'int': 20,
                    'wp': 20,
                    'fel': 20,
                    'a': 1,
                    'w': -1,
                    'sb': -1,
                    'tb': -1,
                    'm': 4,
                    'mag': 0,
                    'ip': 0,
                    'fp': -1,
                    },
                'dwarf_base': {
                    'ws': 30,
                    'bs': 20,
                    's': 20,
                    't': 30,
                    'ag': 10,
                    'int': 20,
                    'wp': 20,
                    'fel': 10,
                    'a': 1,
                    'w': -1,
                    'sb': -1,
                    'tb': -1,
                    'm': 3,
                    'mag': 0,
                    'ip': 0,
                    'fp': -1,
                    },
                'elf_base': {
                    'ws': 20,
                    'bs': 30,
                    's': 20,
                    't': 20,
                    'ag': 30,
                    'int': 20,
                    'wp': 20,
                    'fel': 20,
                    'a': 1,
                    'w': -1,
                    'sb': -1,
                    'tb': -1,
                    'm': 5,
                    'mag': 0,
                    'ip': 0,
                    'fp': -1,
                    },
                'halfling_base': {
                    'ws': 10,
                    'bs': 30,
                    's': 10,
                    't': 10,
                    'ag': 30,
                    'int': 20,
                    'wp': 20,
                    'fel': 30,
                    'a': 1,
                    'w': -1,
                    'sb': -1,
                    'tb': -1,
                    'm': 4,
                    'mag': 0,
                    'ip': 0,
                    'fp': -1,
                    },
                }

    def calc_wounds(self, race, d10result):
        d10result = str(d10result)
        values = {
                'dwarf': {
                        '1': 11, '2': 11, '3': 11,
                        '4': 12, '5': 12, '6': 12,
                        '7': 13, '8': 13, '9': 13,
                        '10': 14,
                    },
                'elf': {
                        '1': 9, '2': 9, '3': 9,
                        '4': 10, '5': 10, '6': 10,
                        '7': 11, '8': 11, '9': 11,
                        '10': 12,
                    },
                'human': {
                        '1': 10, '2': 10, '3': 10,
                        '4': 11, '5': 11, '6': 11,
                        '7': 12, '8': 12, '9': 12,
                        '10': 13,
                    },
                'halfling': {
                        '1': 8, '2': 8, '3': 8,
                        '4': 9, '5': 9, '6': 9,
                        '7': 10, '8': 10, '9': 10,
                        '10': 11,
                    },
                }
        return values[race][d10result]


    def calc_fate_points(self, race, d10result):
        d10result = str(d10result)
        race = str(race)
        values = {
                    'dwarf': {
                         '1': 1, '2': 1, '3': 1, '4': 1,
                         '5': 2, '6': 2, '7': 2, 
                         '8': 3, '9': 3, '10': 3
                        },
                    'elf': {
                         '1': 1, '2': 1, '3': 1, '4': 1,
                         '5': 2, '6': 2, '7': 2, 
                         '8': 2, '9': 2, '10': 2
                        },
                    'halfling': {
                         '1': 2, '2': 2, '3': 2, '4': 2,
                         '5': 2, '6': 2, '7': 2, 
                         '8': 3, '9': 3, '10': 3
                        },
                    'human': {
                         '1': 2, '2': 2, '3': 2, '4': 2,
                         '5': 3, '6': 3, '7': 3, 
                         '8': 3, '9': 3, '10': 3
                        },
                }
        return values[race][d10result]

    def calc_strength_bonus(self,sb_val):
        return sb_val / 10

    def calc_toughness(self, t_val):
        return t_val / 10

    def generate(self, race):
        import copy
        from dice.dice import Dice
        
        result_chars = copy.deepcopy(self.recipies[race +"_base"])
        
        for c in self.stats_plus_2d10:
            result_chars[c] += Dice("2k10").throw()
        result_chars['tb'] = self.calc_toughness(result_chars['t'])
        result_chars['sb'] = self.calc_strength_bonus(result_chars['s'])
        result_chars['w'] = self.calc_wounds(race, Dice("d10").throw())
        result_chars['fp'] = self.calc_fate_points(race, Dice("d10").throw())

        return result_chars


def pretty_table(chars):
    from terminaltables import AsciiTable

    data  = [ list(map(str.upper, ORDER)),  [chars[i] for i in ORDER] ]  
    data2 = [ list(map(str.upper, ORDER2)), [chars[i] for i in ORDER2] ]
    table = AsciiTable(data)
    table2 = AsciiTable(data2)
    return table.table + "\n" + table2.table
