
import chargen.race.dwarf as dwarf
import chargen.race.human as human
import chargen.race.elf as elf
import chargen.race.halfling as halfling
import chargen.career as career
import chargen.characteristics as characteristics
import chargen.talents as talents
import chargen.physique as physique

import random
from collections import namedtuple

class Generator:
    def __init__(self, race=None, sex=None):
        # Basic stuff we need to randomly choose
        if race == None:
            # Here I skew the chances of generating fantasy races
            self.race = random.choice("""human human human human human dwarf dwarf halfling halfling elf""".split()) 
        else:
            self.race = race
        if sex == None:
            self.sex = random.choice("""female male""".split())
        else:
            self.sex = sex

        # XXX rather 'dirty hack' for getting the right module now. I guess
        # when something seems stupid but does its job it's not stupid
        self.race_lib = globals()[self.race].__dict__[self.race.title()]()
        self.race_sec_lib = globals()['human'].__dict__["Human"]()

        # Here we 'generate' the character really
        # because naming things is the real magic :)
        self.name = self.race_lib.ret_name(self.sex)
        self.surname = self.race_lib.ret_surname(self.sex)
        if self.surname == None:
            self.surname = self.race_sec_lib.ret_surname(self.sex)

        # Now for the stats!
        self.chars = characteristics.Characteristics().generate(self.race)
        self.talents = talents.Talents().generate(self.race) 
        self.career = career.Career().ret(self.race)

    def __repr__(self):
        return str(self.race_lib)+"(sex="+self.sex+", name=" + repr(self.name) + ", "+ "surname=" + repr(self.surname)+")"

    def result(self):
        """Return generated character as namedtuple object"""
        character = namedtuple('Character', ['name', 'surname', 'sex',
            'species', 'career', 'char_dict', 'characteristics', 'talents'])
        c = namedtuple('Characteristics', characteristics.ORDER +
                characteristics.ORDER2)
        t = namedtuple('Talents', ['list'])

        return character(name=self.name, surname=self.surname, sex=self.sex,
                species=self.race, career=self.career, char_dict=self.chars,
                characteristics=c(*list(self.chars[k] for k in
                    characteristics.ORDER + characteristics.ORDER2)),
                talents=t(self.talents))

