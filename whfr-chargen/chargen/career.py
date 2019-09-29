
class Career:

    def __init__(self):
        self.name_list = '''agitator apprentice_wizard bailiff barber_surgeon
        boatman bodyguard bone_picker bounty_hunter burgher camp_follower
        charcoal_burner coachman entertainer envoy estalian_diestro ferryman
        fieldwarden fisherman grave_robber hedge_wizard hunter initiate jailer
        kislevite_kossar kithband_warrior marine mercenary messenger militiaman
        miner noble norse_berserker outlaw outrider peasant pit_fighter
        protagonist rat_catcher roadwarden rogue runebearer scribe seaman
        servant shieldbreaker smuggler soldier squire student thief thug
        toll_keeper tomb_robber tradesman troll_slayer vagabond valet watchman
        woodsman zealot'''.split()

        self.available = {
                'dwarf': [0,5,8,11,12,20,22,25,26,28,29,30,32,35,36,37,41,42,43,44,45,46,47,48,49,51,52,53,54,57],
                'elf': [1,12,13,20,24,26,27,32,33,39,41,42,48,49,53,55],
                'halfling': [0,3,6,7,8,9,10,12,15,16,17,18,20,26,27,28,32,34,37,39,43,45,46,48,49,51,52,53,55,56,57],
                'human':[x for x in range(0,60) if x not in [14,17,25,50,54]]
                }

    def ret(self, race):
        import random
        return self.name_list[random.choice(self.available[race])]



