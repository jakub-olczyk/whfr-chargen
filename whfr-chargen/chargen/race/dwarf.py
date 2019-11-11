import random

class Dwarf:

    def __init__(self):
        self.name_element_1 = '''Al Ath Athran Bal Bala Bara Bel Bela Ber Bok
                                Bor Bur Da Dam Dora Drok Drong Dur Dval El Ela
                                Elan Elda Fa Far Fara Fim Fima Firen Fur Fura
                                Ga Gim Gol Gollen Got Gota Grim Gro Grun Hak
                                Haka Har Hega Hur Kad Kar Kata Kaz Kaza Krag
                                Logaz Lok Lun Mo Mola Mor Mora No Nora Nor Nola
                                Noran Nun Oda Oka Olla Olf Oth Othra Ro Ror
                                Roran Ska Skalla Skalf Skar Skor Skora Snor
                                Snora Sven Thar Thor Thora Thron Thrun Thura Un
                                Utha Ulla Vala Var Vara Zak Zaka Zakan Zar Zara
                                Zam Zama Zol Zola
                                '''.split()

        self.name_suffix_male = '''bin bor dil din dok dor drin fin gan gar gil
                                   gin gni grom grond groth grum grund grunt
                                   gon gor grim grin grom gul gun gund ki kin
                                   krag kri krin li lin lik lok lun min mir nin
                                   nir rag ri rig rik rin run skin tan tin
                                   tok trek trok zin zor'''.split()

        self.name_suffix_female = '''bina bora dila dina dokina dora drinella
                                     fina fya gana gara gella gina groma
                                     grondella grotha gruma grunda gruntina
                                     gona gora grimella grina gromina gula
                                     gunella gundina kina kragella krina kya
                                     lina likina loka luna mina mira nina nira
                                     nya ragina riga rika rina runa runella
                                     skina skinella tina toka trekella trekina
                                     troka zina zora'''.split()

    def ret_name(self, sex):
        if sex == 'male':
            return random.choice(self.name_element_1) + random.choice(self.name_suffix_male)
        elif sex == 'female':
            return random.choice(self.name_element_1) + random.choice(self.name_suffix_female)


    def ret_surname(self, sex):
        if sex == 'male':
            return random.choice(self.name_element_1) + random.choice(self.name_suffix_male) + "son"
        elif sex == 'female':
            return random.choice(self.name_element_1) + random.choice(self.name_suffix_female) + "sdotr"
