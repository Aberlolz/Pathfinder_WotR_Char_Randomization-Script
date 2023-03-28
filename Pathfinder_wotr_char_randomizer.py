##############################################################################
##############################IMPORTS#########################################
##############################################################################

import random

##############################################################################
##############################DICTIONARIES####################################
##############################################################################

Pathfinder_Race_Dict =	{
  0: "Human",
  1: "Elf",
  2: "Dwarf",
  3: "Gnome",
  4: "Halfling",
  5: "Half-Elf",
  6: "Half-Orc",
  7: "Aasimar",
  8: "Tiefling",
  9: "Oread",
  10:"Dhampir", 
  11:"Kitsune",
}

Pathfinder_Class_Dict =	{
  0: "Alchemist",
  1: "Arcanist",
  2: "Barbarian",
  3: "Bard",
  4: "Bloodrager",
  5: "Cavalier",
  6: "Cleric",
  7: "Druid",
  8: "Fighter",
  9: "Hunter",
  10:"Inquisitor", 
  11:"Kineticist",
  12:"Magus",
  13:"Monk",
  14:"Oracle",
  15:"Paladin",
  16:"Ranger",
  17:"Rogue",
  18:"Shaman",
  19:"Skald",
  20:"Slayer",
  21:"Sorcerer",
  22:"Warpriest",
  23:"Witch",
  24:"Wizard",
  25:"Shifter",
}

Pathfinder_Mythic_Path_Dict =	{
  0: "Angel",
  1: "Aeon",
  2: "Azata",
  3: "Demon",
  4: "Devil",
  5: "Gold-Dragon",
  6: "Legend",
  7: "Lich",
  8: "Trickster",
  9: "Swarm-That-Walks",
}

Alchemist_Archetypes =	{
  0: "Baseclass",
  1: "Grenadier",
  2: "Vivisectionist",
  3: "Chirurgeon",
  4: "Preservationist",
  5: "Metamorph",
  6: "Incense-Synthesizer",
}

Arcanist_Archetypes =	{
  0: "Baseclass",
  1: "Btown-Fur-Transmuter",
  2: "Eldritch Font",
  3: "Unlettered-Arcanist",
  4: "White-Mage",
  5: "Nature-Mage",
  6: "Phantasmal-Mage",
}

Barbarian_Archetypes =	{
  0: "Baseclass",
  1: "Armored-Hulk",
  2: "Mad-Dog",
  3: "Invulnerable-Rager",
  4: "Beastkin-Beserker",
  5: "Pack-Rager",
  6: "Instinctual-Warrior",
}

Bard_Archetypes =	{
  0: "Baseclass",
  1: "Archaeologist",
  2: "Thundercaller",
  3: "Flame-Dancer",
  4: "Tranquil-Whisperer",
  5: "Dirge-Bard",
  6: "Beast-Tamer",
}

Bloodrager_Archetypes =	{
  0: "Baseclass",
  1: "Bloodrider",
  2: "Greenrager",
  3: "Primalist",
  4: "Spelleater",
  5: "Steelblood",
  6: "Mixed-Blood-Rager",
  7: "Reformed-Fiend",
}

Cavalier_Archetypes =	{
  0: "Baseclass",
  1: "Beast-Rider",
  2: "Disciple-of-the-Pike",
  3: "Knight-of-the-Wall",
  4: "Gendarme",
  5: "Standard-Bearer",
  6: "Fearsome-Leader",
  7: "Cavalier_of_the_Paw",
}

Cleric_Archetypes =	{
  0: "Baseclass",
  1: "Crusader",
  2: "Ecclesithurge",
  3: "Herald-Caller",
  4: "Demonbane-Priest",
  5: "Angelfire-Apostle",
  6: "Priest-of-Balance",
}

Druid_Archetypes =	{
  0: "Baseclass",
  1: "Blight-Druid",
  2: "Feyspeaker",
  3: "Defender-of-the-True-World",
  4: "Drovier",
  5: "Elemental-Rampager",
  6: "Primal-Druid",
}

Fighter_Archetypes =	{
  0: "Baseclass",
  1: "Aldori-Defender",
  2: "Two-Handed-Fighter",
  3: "Tower-Shield-Specialist",
  4: "Dragonheir-Scion",
  5: "Armiger",
  6: "Mutation-Warrior",
}

Hunter_Archetypes =	{
  0: "Baseclass",
  1: "Divine-Hunter",
  2: "Urban-Hunter",
  3: "Colluding-Scoundrel",
  4: "Forester",
  5: "Wandering-Marksman",
  6: "Divine-Hound",
}

Inquisitor_Archetypes =	{
  0: "Baseclass",
  1: "Monster-Tactician",
  2: "Tactical-Leader",
  3: "Sacred-Huntsmaster",
  4: "Faith-Hunter",
  5: "Sanctified-Slayer",
  6: "Judge",
}

Kineticist_Archetypes =	{
  0: "Baseclass",
  1: "Dark-Elementalist",
  2: "Psychokineticist",
  3: "Kinetic-Knight",
  4: "Blood-Kineticist",
  5: "Overwhelming-Soul",
  6: "Elemental-Engine",
}

Magus_Archetypes =	{
  0: "Baseclass",
  1: "Eldritch-Scion",
  2: "Sword-Saint",
  3: "Eldritch-Archer",
  4: "Hexcrafter",
  5: "Armored-Battlemage",
  6: "Arcane-Rider",
  7: "Spell-Dancer",
}

Monk_Archetypes =	{
  0: "Baseclass",
  1: "Scaled-Fist",
  2: "Sensei",
  3: "Traditional-Monk",
  4: "Zen-Archer",
  5: "Sohei",
  6: "Quarterstaff-Master",
  7: "Student-of-Stone",
}

Oracle_Archetypes = {
  0: "Baseclass",
  1: "Lone-Strider",
  2: "Enlightened-Philosopher",
  3: "Divine-Herbalist",
  4: "Seeker",
  5: "Possessed-Oracle",
  6: "Wind-Whisperer",
  7: "Purifier",
}

Paladin_Archetypes =	{
  0: "Baseclass",
  1: "Divine-Hunter",
  2: "Hospitaler",
  3: "Divine-Guardian",
  4: "Warrior-of-the-Holy-Light",
  5: "Martyr",
  6: "Divine-Scion",
  7: "Stonelord",
}

Ranger_Archetypes =	{
  0: "Baseclass",
  1: "Freebooter",
  2: "Stormwalker",
  3: "Flame-Warden",
  4: "Espionage-Expert",
  5: "Demonslayer",
  6: "Nomad",
}

Rogue_Archetypes =	{
  0: "Baseclass",
  1: "Eldritch-Scoundrel",
  2: "Knife-Master",
  3: "Thug",
  4: "Sylvan-Trickster",
  5: "Underground-Chemist",
  6: "Rowdy",
  7: "Master-of-All"
}

Shaman_Archetypes =	{
  0: "Baseclass",
  1: "Possessed-Shaman",
  2: "Spirit-Hunter",
  3: "Spirit-Warden",
  4: "Unsworn-Shaman",
  5: "Witch-Doctor",
  6: "Shadow-Shaman",
  7: "Wildland-Shaman",
}

Skald_Archetypes =	{
  0: "Baseclass",
  1: "Battle-Scion",
  2: "Court-Poet",
  3: "Demon-Dancer",
  4: "Herald-of-the-Horn",
  5: "Hunt-Caller",
  6: "Battler-Singer",
}

Slayer_Archetypes =	{
  0: "Baseclass",
  1: "Vanguard",
  2: "Deliverer",
  3: "Spawn-Slayer",
  4: "Arcane-Enforcer",
  5: "Executioner",
  6: "Stygian-Slayer",
  7: "Imitator",
}

Sorcerer_Archetypes =	{
  0: "Baseclass",
  1: "Empyreal-Sorcerer",
  2: "Sage-Sorcerer",
  3: "Sylvan-Sorcerer",
  4: "Crossblooded",
  5: "Seeker",
  6: "Overwhelming-Mage",
  7: "Nine-Tailed-Heir",
}

Warpriest_Archetypes =	{
  0: "Baseclass",
  1: "Champion-of-the-Faith",
  2: "Cult-Leader",
  3: "Feral-Champion",
  4: "Disenchanter",
  5: "Shieldbearer",
  6: "Proclaimer",
}

Witch_Archetypes =	{
  0: "Baseclass",
  1: "Stygmatized-Witch",
  2: "Hagsbound",
  3: "Hex-Channeler",
  4: "Ley-Line-Guardian",
  5: "Elemental-Witch",
}

Wizard_Archetypes =	{
  0: "Baseclass",
  1: "Arcane-Bomber",
  2: "Scroll-Savant",
  3: "Thassilionian-Specialist",
  4: "Exploiter-Wizard",
  5: "Elemental-Specialist",
  6: "Spell-Master",
  7: "Cruoromancer"
}

Shifter_Archetypes =	{
  0: "Baseclass",
  1: "Griffonheart-Shifter",
  2: "Child-of-Manticore",
  3: "Dragonblood-Shifter",
  4: "Feyform-Shifter",
  5: "Fiendflesh-Shifter",
  6: "Rageshaper",
  7: "Wild-Effigy"
}

##############################################################################
#########################WHERE#THE#MAGIC#HAPPENS##############################
##############################################################################

Pathfinder_Race_RNG = random.randrange(len(Pathfinder_Race_Dict))
Pathfinder_Class_RNG = random.randrange(len(Pathfinder_Class_Dict))
Pathfinder_Mythic_Path_RNG = random.randrange(len(Pathfinder_Mythic_Path_Dict))

print("Race is:\t",Pathfinder_Race_Dict[Pathfinder_Race_RNG])
print("Class is:\t",Pathfinder_Class_Dict[Pathfinder_Class_RNG])

match Pathfinder_Class_RNG:
    case 0:
        Pathfinder_Archetype_RNG = random.randrange(len(Alchemist_Archetypes))
        print("Archetype is:\t", Alchemist_Archetypes[Pathfinder_Archetype_RNG])
    case 1:
        Pathfinder_Archetype_RNG = random.randrange(len(Arcanist_Archetypes))
        if Pathfinder_Race_RNG != 3:
            while Pathfinder_Archetype_RNG == len(Arcanist_Archetypes):
               Pathfinder_Archetype_RNG = random.randrange(len(Arcanist_Archetypes))
        print("Archetype is:\t", Arcanist_Archetypes[Pathfinder_Archetype_RNG])
    case 2:
        Pathfinder_Archetype_RNG = random.randrange(len(Barbarian_Archetypes))
        print("Archetype is:\t", Barbarian_Archetypes[Pathfinder_Archetype_RNG])
    case 3:
        Pathfinder_Archetype_RNG = random.randrange(len(Bard_Archetypes))
        print("Archetype is:\t", Bard_Archetypes[Pathfinder_Archetype_RNG])
    case 4:
        Pathfinder_Archetype_RNG = random.randrange(len(Bloodrager_Archetypes))
        if Pathfinder_Race_RNG != 8:
            while Pathfinder_Archetype_RNG == len(Bloodrager_Archetypes):
              Pathfinder_Archetype_RNG = random.randrange(len(Bloodrager_Archetypes))
        print("Archetype is:\t", Bloodrager_Archetypes[Pathfinder_Archetype_RNG])
    case 5:
        Pathfinder_Archetype_RNG = random.randrange(len(Cavalier_Archetypes))
        if Pathfinder_Race_RNG != 4:
            while Pathfinder_Archetype_RNG == len(Cavalier_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Cavalier_Archetypes))
        print("Archetype is:\t", Cavalier_Archetypes[Pathfinder_Archetype_RNG])
    case 6:
        Pathfinder_Archetype_RNG = random.randrange(len(Cleric_Archetypes))
        print("Archetype is:\t", Cleric_Archetypes[Pathfinder_Archetype_RNG])
    case 7:
        Pathfinder_Archetype_RNG = random.randrange(len(Druid_Archetypes))
        print("Archetype is:\t", Druid_Archetypes[Pathfinder_Archetype_RNG])
    case 8:
        Pathfinder_Archetype_RNG = random.randrange(len(Fighter_Archetypes))
        print("Archetype is:\t", Fighter_Archetypes[Pathfinder_Archetype_RNG])
    case 9:
        Pathfinder_Archetype_RNG = random.randrange(len(Hunter_Archetypes))
        print("Archetype is:\t", Hunter_Archetypes[Pathfinder_Archetype_RNG])
    case 10:
        Pathfinder_Archetype_RNG = random.randrange(len(Inquisitor_Archetypes))
        print("Archetype is:\t", Inquisitor_Archetypes[Pathfinder_Archetype_RNG])
    case 11:
        Pathfinder_Archetype_RNG = random.randrange(len(Kineticist_Archetypes))
        print("Archetype is:\t", Kineticist_Archetypes[Pathfinder_Archetype_RNG])
    case 12:
        Pathfinder_Archetype_RNG = random.randrange(len(Magus_Archetypes))
        if Pathfinder_Race_RNG != 1:
            while Pathfinder_Archetype_RNG == len(Magus_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Magus_Archetypes))
        print("Archetype is:\t", Magus_Archetypes[Pathfinder_Archetype_RNG])
    case 13:
        Pathfinder_Archetype_RNG = random.randrange(len(Monk_Archetypes))
        if Pathfinder_Race_RNG != 9:
            while Pathfinder_Archetype_RNG == len(Monk_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Monk_Archetypes))
        print("Archetype is:\t", Monk_Archetypes[Pathfinder_Archetype_RNG])
    case 14:
        Pathfinder_Archetype_RNG = random.randrange(len(Oracle_Archetypes))
        if Pathfinder_Race_RNG != 0:
            while Pathfinder_Archetype_RNG == len(Oracle_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Oracle_Archetypes))
        print("Archetype is:\t", Oracle_Archetypes[Pathfinder_Archetype_RNG])
    case 15:
        Pathfinder_Archetype_RNG = random.randrange(len(Paladin_Archetypes))
        if Pathfinder_Race_RNG != 2:
            while Pathfinder_Archetype_RNG == len(Paladin_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Paladin_Archetypes))
        print("Archetype is:\t", Paladin_Archetypes[Pathfinder_Archetype_RNG])
    case 16:
        Pathfinder_Archetype_RNG = random.randrange(len(Ranger_Archetypes))
        print("Archetype is:\t", Ranger_Archetypes[Pathfinder_Archetype_RNG])
    case 17:
        Pathfinder_Archetype_RNG = random.randrange(len(Rogue_Archetypes))
        if Pathfinder_Race_RNG != 5:
            while Pathfinder_Archetype_RNG == len(Rogue_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Rogue_Archetypes))
        print("Archetype is:\t", Rogue_Archetypes[Pathfinder_Archetype_RNG])
    case 18:
        Pathfinder_Archetype_RNG = random.randrange(len(Shaman_Archetypes))
        if Pathfinder_Race_RNG != 6:
            while Pathfinder_Archetype_RNG == len(Shaman_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Shaman_Archetypes))
        print("Archetype is:\t", Shaman_Archetypes[Pathfinder_Archetype_RNG])
    case 19:
        Pathfinder_Archetype_RNG = random.randrange(len(Skald_Archetypes))
        print("Archetype is:\t", Skald_Archetypes[Pathfinder_Archetype_RNG])
    case 20:
        Pathfinder_Archetype_RNG = random.randrange(len(Slayer_Archetypes))
        if Pathfinder_Race_RNG != 0:
            while Pathfinder_Archetype_RNG == len(Slayer_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Slayer_Archetypes))
        print("Archetype is:\t", Slayer_Archetypes[Pathfinder_Archetype_RNG])
    case 21:
        Pathfinder_Archetype_RNG = random.randrange(len(Sorcerer_Archetypes))
        if Pathfinder_Race_RNG != 11:
            while Pathfinder_Archetype_RNG == len(Sorcerer_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Sorcerer_Archetypes))
        print("Archetype is:\t", Sorcerer_Archetypes[Pathfinder_Archetype_RNG])
    case 22:
        Pathfinder_Archetype_RNG = random.randrange(len(Warpriest_Archetypes))
        print("Archetype is:\t", Warpriest_Archetypes[Pathfinder_Archetype_RNG])
    case 23:
        Pathfinder_Archetype_RNG = random.randrange(len(Witch_Archetypes))
        print("Archetype is:\t", Witch_Archetypes[Pathfinder_Archetype_RNG])
    case 24:
        Pathfinder_Archetype_RNG = random.randrange(len(Wizard_Archetypes))
        if Pathfinder_Race_RNG != 10:
            while Pathfinder_Archetype_RNG == len(Wizard_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(Wizard_Archetypes))
        print("Archetype is:\t", Wizard_Archetypes[Pathfinder_Archetype_RNG])
    case 25:
        Pathfinder_Archetype_RNG = random.randrange(len(Shifter_Archetypes))
        print("Archetype is:\t", Shifter_Archetypes[Pathfinder_Archetype_RNG])
    case _:
        print("I am Error")


print("Mythic Path is:\t",Pathfinder_Mythic_Path_Dict[Pathfinder_Mythic_Path_RNG])
input("Press Enter to Exits...")