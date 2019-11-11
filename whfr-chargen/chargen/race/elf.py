import random
class Elf:

    def __init__(self):
        self.name_element = '''Aed Ael Aelf Aen Aeth Alth An And Ar Arg Ast
                                 Ath Av Ban Bel Beth Cad Cael Caem Caeth Cal
                                 Cam Cel Cir El Eld Elth En End Er Ers Fand Fer
                                 Ferg Fim Fin Gal Gald Gaen Gaes Ged Gen Ges
                                 Geth Glor Has Hath Hel Heth Hith Ill Ind Ist
                                 Ith Iy Cor Cy Cyr La Lan Lil Lim Lih Loth Mal
                                 Mar Mas Math Me Mes Meth Men Mor Mort Nal Nar
                                 Nen Nor Norl Ri Riabb Riann Rid Riell Rien
                                 Ruth Ryn Tab Tal Tan Tar Teth Tel Tor Ty Ul Um
                                 Ur Yr Yv Yav Yuv Val Viv'''.split()

        self.name_element_middle = '''a al an ar as e el en er es fan fen fin i
                                      il in ir is o ol on or os ra ral ran re
                                      rel ren ri ril rin ro rol ron ry sa sal
                                      san se sel sen si sil sin so sol son u
                                      ul'''.split()

        self.name_element_male = '''baen baine baire bar bhir brier brior brin
                                    daen daine daire dar dhil dhir drel drid
                                    dror dwe eorl eos eoth eod fil din dir hil hin
                                    hir hor il in ion ir is ith id lael laen
                                    laer laine laire lan las len les lil lin
                                    lir lis lor los mael maen mair main mal mar
                                    mil min mir nael naen naer nail nair nal
                                    nan nar neal nean near nil nin nir nis ran
                                    rea rel ril riol rion rior riorl riorn rir
                                    ryel taen tair tain than thar thel thil
                                    thir thin thril thrin thwe til tin tis we
                                    yan'''.split()

        self.name_element_female = '''a aine am ann arma arna arth ath beann
                                      bet beth brim brys deann det deth dys
                                      drian driel drys eann eanna earna earth
                                      elle eth eys eyth felle fionn flys fyll
                                      fynn fyr fys i ille ina ira isa ithi itt
                                      la lam lana larna lath leann leath lel
                                      lelle leth let lielle lieth lyann nelle
                                      nem neth ni niell niella nith ras reann
                                      rell relle rielle ris rith rys seth sith
                                      sor soth sys tar teal teann ter thea ther
                                      thi thryn thyn tir tor tos tryan trys yll
                                      yrs ys'''.split()

        self.surname_last = '''ain thadh nain hail again aghil hil odh adh ildh
                               ildh naigh laigh caigh idigh ithigh aird airth
                               airdh edh and heid uibh lain tain bain
                               bhain'''.split()

    def ret_name(self, sex, middle=True):
        name = ""
        name += random.choice(self.name_element)
        if middle == True:
            name += random.choice(self.name_element_middle)
        if sex == 'male':
            name += random.choice(self.name_element_male)
        elif sex == 'female':
            name += random.choice(self.name_element_female)
        return name

    def ret_surname(self, sex):
        surname = ""
        surname += random.choice(self.name_element)
        surname += random.choice(self.name_element_middle)
        surname += random.choice(self.surname_last)
        return surname


