
class Talents:

    def __init__(self):
        self.talent_list = '''acute_hearing ambidextrous coolheaded excellent_vision fleet_footed hardy
                           lightening_reflexes luck marksman mimic night_vision
                           resistance_to_disease resistance_to_magic
                           resistance_to_poison savvy sixth_sense strong_minded
                           sturdy suave super_numerate very_resilient
                           very_strong warrior_born
                           '''.split()
        self.race_chances = {
                'halfling': {
                    '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 1, '7': 1,
                    '8': 1, '9': 1, '10': 1, '11': 2, '12': 2, '13': 2, '14':
                    2, '15': 2, '16': 3, '17': 3, '18': 3, '19': 3, '20': 3,
                    '21': 4, '22': 4, '23': 4, '24': 4, '25': 4, '26': 5, '27':
                    5, '28': 5, '29': 5, '30': 6, '31': 6, '32': 6, '33': 6,
                    '34': 7, '35': 7, '36': 7, '37': 7, '38': 7, '39': 8, '40':
                    8, '41': 8, '42': 8, '43': 9, '44': 9, '45': 9, '46': 9,
                    '47': 9, '48': 11, '49': 11, '50': 11, '51': 11, '52': 12,
                    '53': 12, '54': 13, '55': 13, '56': 13, '57': 13, '58': 14,
                    '59': 14, '60': 14, '61': 14, '62': 14, '63': 15, '64': 15,
                    '65': 15, '66': 15, '67': 15, '68': 16, '69': 16, '70': 16,
                    '71': 16, '72': 16, '73': 17, '74': 17, '75': 17, '76': 17,
                    '77': 17, '78': 18, '79': 18, '80': 18, '81': 18, '82': 18,
                    '83': 19, '84': 19, '85': 19, '86': 19, '87': 19, '88': 20,
                    '89': 20, '90': 20, '91': 20, '92': 21, '93': 21, '94': 21,
                    '95': 21, '96': 22, '97': 22, '98': 22, '99': 22, '100': 22,
                    },
                'human': {
                    '1': 0, '2': 0, '3': 0, '4': 0, '5': 1, '6': 1, '7': 1,
                    '8': 1, '9': 1, '10': 2, '11': 2, '12': 2, '13': 2, '14':
                    3, '15': 3, '16': 3, '17': 3, '18': 3, '19': 4, '20': 4,
                    '21': 4, '22': 4, '23': 5, '24': 5, '25': 5, '26': 5, '27':
                    5, '28': 6, '29': 6, '30': 6, '31': 6, '32': 7, '33': 7,
                    '34': 7, '35': 7, '36': 8, '37': 8, '38': 8, '39': 8, '40':
                    8, '41': 9, '42': 9, '43': 9, '44': 9, '45': 10, '46': 10,
                    '47': 10, '48': 10, '49': 10, '50': 11, '51': 11, '52': 11,
                    '53': 11, '54': 12, '55': 12, '56': 12, '57': 12, '58': 13,
                    '59': 13, '60': 13, '61': 13, '62': 14, '63': 14, '64': 14,
                    '65': 14, '66': 14, '67': 15, '68': 15, '69': 15, '70': 15,
                    '71': 15, '72': 16, '73': 16, '74': 16, '75': 16, '76': 17,
                    '77': 17, '78': 17, '79': 17, '80': 18, '81': 18, '82': 18,
                    '83': 18, '84': 19, '85': 19, '86': 19, '87': 19, '88': 20,
                    '89': 20, '90': 20, '91': 20, '92': 21, '93': 21, '94': 21,
                    '95': 21, '96': 22, '97': 22, '98': 22, '99': 22, '100': 22,
                    }
                }

    def ret(self, percent, race):
        percent = str(percent)
        return self.talent_list[self.race_chances[race][percent]]


    def generate(self, race):
        from dice.dice import Dice
        import random

        talents = []
        if race == "human":
            for i in range(2):
                try:
                    last_talent = talents[-1]
                except:
                    last_talent = None

                while(1):
                    talent = self.ret(Dice("d100").throw(), race)
                    if talent != last_talent:
                        break
                talents.append(talent)

        elif race == "halfling":
            for i in """night_vision resistance_to_chaos specialist_weapon_sling""".split():
                talents.append(i)

            while(1):
                talent = self.ret(Dice("d100").throw(), race)
                if talent not in talents:
                    break
            talents.append(talent)

        elif race == "dwarf":
            talents = """dwarfcraft grudgeborn_fury night_vision resistance_to_magic stouthearted sturdy""".split()

        elif race == "elf":
            talents = """excellent_vision night_vision""".split()
            talents.append(random.choice("""coolheaded savvy""".split()))
            talents.append(random.choice("""aethyric_attunement specialist_weapon_longbow""".split()))

        return talents

def pretty_list(talents):
    _list = ""
    for i in talents:
        _list += "* " + str(i) + "\n"
    return _list
