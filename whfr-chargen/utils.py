# mainly stuff for pretty printing

import chargen.talents as talents
import chargen.characteristics as characteristics

# XXX rewrite class funtions into this interface : for now use this as wrappers

def characteristics_table(c):
    return characteristics.pretty_table(c)

def talents_table(t):
    return talents.pretty_list(t)

# The original method from Generator class to emulate
#
#    def print_screen(self):
#        print "-" * 55 
#        msg_str = "Name: {} {}\nSex: {}\nRace: {}\nProfession: {}"
#        chars_table = characteristics.pretty_table(self.chars)
#        talents_list = talents.pretty_list(self.talents)
#        print msg_str.format(self.name, self.surname,self.sex,self.race,self.career)  
#        print "\nCharacteristics table"
#        print chars_table 
#        print "\nTalents list"
#        print talents_list

def print_character(character, is_printing=True):
    result = '-' * 55 + '\n'
    msg_str = "Name: {} {}\nSex: {}\nRace: {}\nProfession: {}\n"
    chars_table = characteristics_table(character.char_dict)
    talents_list = talents_table(character.talents.list)
    result += msg_str.format(character.name, character.surname, character.sex,
            character.species, character.career)  
    result += "Characteristics table\n"
    result += chars_table + '\n'
    result += "Talents list\n"
    result += talents_list + '\n'
    if is_printing:
        print(result)
    else:
        return result
        
