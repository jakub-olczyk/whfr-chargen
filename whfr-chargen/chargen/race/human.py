import random

class Human:
    
    def __init__(self):
        self.names_female = '''Abbie Abighild Abighund Abighunda Ada Adel 
                Adelind Adeline Adelyn Adelle Agathe Agnete Aldreda Alfreda
                Alicia Allane Althea Amalie Amalinde Amalyn Anhidla Annabella
                Anna Anthea Arabella Aver Bechilda Bellane Bella Benedicta
                Berlinda Berlyn Bertha Berthilda Bess Beth Broncea Brunhilda
                Camilla Carla Carlinda Carlotta Cilicia Cilie Clora Clothilda
                Connie Constance Constanza Cordelia Dema Demona Desdemona
                Dorthilda Drachena Drachilda Edhilda Edith Edyth Edythe Eleanor
                Elinor Elisinda Elisina Ella Ellene Ellinde Eloise Elsa Elsbeth
                Elspeth Elyn Emagunda Emelia Emme Emmalyn Emmanuel Emerlinde
                Emerlyn Erica Ermina Eminlind Ermintrude Esmeralda Estelle
                Etheldreda Ethelind Ethelreda Fay Frieda Friedhilda Friedrun
                Friedrica Gabby Gabriele Galina Gena Genevieve Genoveva
                Gerberga Gerda Gerlinde Gertie Gertrud Greta Gretchen Grizelda
                Grunhilda Gudrun Gudryn Hanna Hedwig Heidi Heidrun Helga
                Herlinde Herwig Hilda Hildegart Hildegund Honoria Ida Ingrid
                Ingrun Ingrund Irmella Irmine Isabella Isadora Isolde Jocelin
                Johanna Josie Karin Katarine Katheryn Katharina Katerine
                Keterlind Keterlyn Kityn Kristen Kristena Kristyn Kirsten
                Kirstyn Lavina Lavinia Leanor Leanora Leticia Letty Lena Lenora
                Lisa Lisbeth Lizzie Lorinda Lorna Lucinda Lucretia Lucie
                Ludmilla Mabel Madge Magdalyn Maggie Maghilda Maglind Maglyn
                Magunda Magreta Maida Marien Marietta Margaret Margareta
                Marline Marlyn Mathilda Maude May Meg Melicent Miranda Moll
                Nathilda Nellie Nora Olga Ophelia Osterhild Ostelle Ostia
                Ottagunda Ottaline Ottilda Ottlyn Perdita Pergale Pergunda
                Petronella Philomelia Reikhilda Renata Rosabel Rosabella Rosale
                Rosalia Rosalin Rosalinde Rosamunde Rosanne Rose Roz Rozhilda
                Salina Saltza Sigismunda Sigrid Sigunda Solla Styrine Talima
                Theodora Therese Tilea Ursula Ulrica Valeria Verena Wilfrieda
                Wilhelmina Winifred Wolfhilde Zemelda Zena'''.split()

        self.names_male = '''Abelhard Abelhelm Admund Adred Adric Agis Alaric
                Alberic Albrecht Aldebrand Aldred Aldric Alfreid Altmar Alric
                Andre Andred Andric Anshelm Anton Arne Arnulf Axel Axelbrand
                Baldred Baldric Baldwin Balthasar Barnabas Bart Bartolf
                Bartomar Bernolt Bertold Bertolf Boris Bruno Burgolf Calvin
                Casimir Caspar Cedred Conrad Corvin Dagmar Dankmar Dankred
                Dekmar Detlef Diebold Diel Dietfried Dieter Dietmar Dietmund
                Dietrich Dirk Donat Durnhelm Eber Eckel Eckhart Edgar Edmund
                Edwin Ehrhart Ehrl Ehrwig Eldred Elmeric Emil Engel Engelbert
                Engelbrecht Engelhart Eodred Eomund Erdman Erdred
                Erkenbrand Erasmus Erich Erman Ernst Erwin Eugen Eustasius
                Ewald Fabian Faustus Felix Ferdinand Fleugweiner Fosten Franz
                Frediger Fredric Friebald Friedrich Gawin Gerber Gerhart
                Gerlach Gernar Gerolf Gilbrecht Gisbert Giselbrecht Gismar
                Goran Gosbert Goswin Gotfried Gothard Gottolf Gotwin Gregor
                Greimold Grimwold Griswold Guido Gundolf Gundred Gunnar Gunter
                Gunther Gustaf Hadred Hadwin Hagar Hagen Haldred Halman Hamlyn
                Hans Harbrand Harman Hartmann Haug Heidric Heimar Heinfried
                Heinman Heinrich Heinz Helmut Henlyn Hermann Herwin Hieronymus
                Hildebart Hildebrand Hildemar Hildemund Hildred Hildric Horst
                Hugo Igor Ingwald Jander Jekil Jodokus Johann Jonas Jorg Jorn
                Josef Jost Jurgen Karl Kaspar Klaus Kleber Konrad Konradin Kurt
                Lamprecht Lanfried Lanric Lenwin Leo Leopold Levin Liebert
                Liebrecht Liebwin Lienhart Linus Lodwig Lothar Lucius Ludwig
                Luitpold Lukas Lupold Lupus Luther Lutolf Madred Magnus Mandred
                Manfred Mathias Max Maximilian Meiner Meinhart Meinolf Mekel
                Merkel Nat Nathandar Nicodemus Odamar Odric Odwin Olbrecht
                Oldred Oldric Ortlieb Ortolf Orwin Oswald Osric Oswin Otfried
                Otto Otwin Paulus Prospero Ragen Ralf Rambrecht Randulf Ranulf
                Ranald Reikhard Reikmar Rein Reiner Reinmar Reinhart Reinolt
                Reuban Reynevan Rigo Roderic Rolf Ruben Rudel Rudgar Rudolf
                Rufus Ruprecht Sebastian Semund Sepp Sieger Siegfried Sigismund
                Sigmund Sigric Steffen Tankred Theoderic Tilmann Tomas Trubald
                Trubert Udoderic Tilmann Tomas Trubald Trubert Udoderic Tilmann
                Tomas Trubald Trubert Udo Ulli Ulfred Ulfman Ulman Uto Valdred
                Valdric Varl Viggo Viktor Vilmar Volker Volmar Volkrad Volkin
                Voltz Walbrecht Waldor Waldred Walther Warmund Werner Wilbert
                Wilfred Wilfried Wilhelm Woldred Wolfram Wolfhart Wolfgang Wulf
                Xavier '''.split()

        self.surnames = '''Adelhof Albrecht Allenstag Altmann Atzwig Bacher
                Baer Baumann Becker Behn Betz Beyer Bischof Boehm Breitenbach
                Breuer Dahmbach Delfholt Drakenhof Drauwulf Durrbein Ehrhard
                Eisenhauer Eschlimann Falkenheim Falkenbach Fehr Fiegler
                Fleischer Frohlich Frueh Fuchs Gaffwig Gaertner Gebauer
                Godtgraf Grunenwald Guth Haintz Herz Herzog Hirtzel Hoch Hoefer
                Hofstetter Jaeger Jochutz Jutzenbach Kalb Kaltenbach Kraemer
                Krebs Kuhn Kummel Konig Konigsamen Lang Lankdorf Liess Lebengut
                Lutzen Machholt Mausmann Meyer Mohr Muller Nachtmann Naubhof
                Netzhoch Neumann Niederlitz Nuhr Oberholtzer Ohrsten Otzlowe
                Reichert Reifsneider Riese Rohrig Reiss Schaffer Schaumer
                Scherer Schultz Schleidermacher Schreiber Schwalb Steiner
                Tabbeck Tauber Tolzen Traschsel Weber Wechsler Wirtz Widmann
                Widmer Veit Vogt Vogel Zumwald'''.split()
        

    def ret_name(self, sex):
        if sex == 'male':
            return random.choice(self.names_male)
        elif sex == 'female':
            return random.choice(self.names_female)

    def ret_surname(self, sex):
        return random.choice(self.surnames)
