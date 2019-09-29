import random

class Halfling:

    def __init__(self):
        
        self.name_element = '''Bag Balf Berc Bill Bobb Bodg Bog Bom Bonn Brog
                            Bulc Bull Bust Cam Cap Ced Chund Clog Clof Cob Cog
                            Crum Crump Curl  Dod Dog Dott Dram Drub Drog Dron
                            Durc Elm Enn Ermin Ethan Falc Falm Fald Far Fild
                            Flac Fogg Frit Ful Func Gaff Galb Gert Gamm Giff
                            Gild Gon Grop Gudd Gump Ham Hal Hart Harp Yarp Yac
                            Yasp Yoc Lac Lil Lob Lott Lud Lurc Mad Mag Man May
                            Mer Mul Murc Murd Nag Nell Nobb Od Og Old Pipp Podd
                            Porc Riff Rip Rob Sam Supp Taff Talb Talc Tay Tom
                            Wald Watt Will'''.split()

        self.name_male = '''belly er fast in it mutch o odoc riadoc regar wick
                            wise wit y'''.split()

        self.name_female = '''a adell alot apple bell berry eena ella era et ia
                              flower lotta petal riella sweet trude rose willow
                              y'''.split()

    def ret_name(self, sex):
        name = random.choice(self.name_element)
        if sex == 'male':
            name += random.choice(self.name_male)
        elif sex == 'female':
            name += random.choice(self.name_female)
        return name

    def ret_surname(self,sex):
        return None
