import random

class Physique:

    def __init__(self):
        self.distinguishing_marks = '''pox_marks ruddy_faced scar tattoo
                                       earring ragged_ear nose_ring wart
                                       broken_nose missing_tooth snaggle_teeth
                                       lazy_eye missing_eyebrow missing_digit
                                       missing_nail distinctive_gait
                                       curious_smell huge_nose large_mole
                                       small_bald_patch
                                       strange_coloured_eye'''.split()
        self.birth_place = {
                    'elf': '''city_altdorf city_marienburg laurelorn_forest great_forest reikwald_forest'''.split(),
                    'human': '''averland hochland middenland nordland ostermark ostland reikland stirland talabecland wissenland'''.split(),
                    'dwarf': '''karak_nom karak_izor karak_hirn karak_kadrin karak_a_karak zhufbar barak_varr'''.split(),
                    'halfling': '''averland hochland middenland nordland ostermark ostland reikland stirland talabecland wissenland'''.split(),
                }
        self.birth_human = '''city prosperous_town market_town fortified_town farming_village poor_village small_settlement pig_farm cattle_farm arable_farm hovel'''.split()
        random.shuffle(self.birth_human)
        random.shuffle(self.birth_place['elf'])
        random.shuffle(self.birth_place['dwarf'])
        random.shuffle(self.birth_place['human'])

        self.age = {
                    'dwarf': range(20,115,5),
                    'elf': range(30,125,5),
                    'halfling': range(20,60,2),
                    'human': range(16,35,1)
                }

    def ret_age(self,race):
        return random.choice(self.age[race]) + random.randint(0,10) if race != 'human' else 0

    def ret_mark(self):
        return random.choice(self.distinguishing_marks)

    def ret_birthplace(self, race):
        place = random.choice(self.birth_place[race])
        additional = ""
        if race == 'human' or race == 'halfling':
            additional = " " + random.choice(self.birth_human)
            if race == 'halfling' and random.randint(0,100) < 50:
                return 'moot'
        elif race == 'dwarf':
            if random.randint(0,100) < 30:
                additional = random.choice(self.birth_place['human']) + " " + random.choice(self.birth_human)
                return additional
        return place + additional

