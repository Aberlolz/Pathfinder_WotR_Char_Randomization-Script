##############################################################################
##############################IMPORTS#########################################
##############################################################################

import random
import races
import classes
import mythics
import archetypes

##############################################################################
#########################WHERE#THE#MAGIC#HAPPENS##############################
##############################################################################

# Don't judge my Code please, here's a Dinosaur on a Bycicle.
#                                                                                                               
#                                                          --; .!   ??!                                         
#                                                     :QQQ?>>>???HQQ??Q                                         
#                                                   HQ??QMMHHQ?77HHQQ?>?>7H                                     
#                                                  HQ?Q?QQHMHQ?7>777777?7>>>?Q                                  
#                                                  QQQQ?Q??Q7:?>!>7>>!>>7>>?>7>                                 
#                                                 !HQHQ?>>?>>>>>777>>>>!>>>>:!7?                                
#                                                 ;HQQ?H?>>>>>>>7777>>>>>>>>!>?M                                
#                                 QHHHH           .HH?7???7>::!?>H?>777>>?H??>7                                 
#                               Q??QQ??QHHHH      HQQ?Q??????77777?Q?H????7?HM!                                 
#                             ?QQQQQQQ?????HHHHQQ-QHHQQQ????QHQHQ?QQQHHHMMMQ                                    
#                            Q???Q??????7?????QQQQQ?QQQQMMMMMMMMMM                                              
#                           ?QQ?QQ??7777>77??????Q??QQQQHMMHHMM                                                 
#                           Q?QQQ???777>7????7??????QQQMMHM                                                     
#   >MHHQQQQQQHQQQQQHQHHQQQQQ?Q?H????7>>>777>7??????QQMMMM                                                      
#         MHQQQQ??Q??Q?Q?QQ?????Q???777>!:>>>7????QQHMHHMH.                                                     
#            QHQQQ?????Q?Q?????HM????7>>!-:>>77??QHMMMMMMQHH                                                    
#              ;HHQQ?????QQ????QH????7>>-:>77???HMMMMMMMMQQM                                                    
#                 HHHQ??????????QH????7>>>7Q????QHMMMMMMHHHH                                                    
#                    M???????777QHHMHH????QMH???QHMMMMM;  H??                                                   
#                     Q?Q????77?QHHHMMM7?QMMMQ?QHMMMMMQHM  !?!?                                                 
#                     .Q?????????HHHMMM7:?MMMMMMMMMM???QHM   ?>!-                                               
#                      QQQQ?Q????QHMMMM7>Q???MMH????7??QHM      -7!?                                            
#                       QQ???????QHMMMH>>QQHM .HHQQ????QHM         77>                                          
#                        Q?Q????QHMQHQHH>HM?  77>>>7?QHMM         H?HQ?                                         
#                         Q?????QHM  .- >>7  ?>7????HHM       7  HQ;                                            
#                          Q????QHM     ;7>: 7????HMH          MH                                               
#                          -QQ?QQHMHH   7Q?H77??HM7   ;  >MHMM!M                                                
#                           HQQQHMMH   :?QQHHMMM   >MHMM   -  M                                                 
#                            ??QHM;:M ?.   >>7H HMMM   !   .QM                                                  
#                           ????HHM H7      >>>M    MM;   ? H                                                   
#                           ????QHM  M       ::7H!   >M> >>>MHM                                                 
#                            ????HM   Q;     >>!?HM  7MHM>>!                                                    
#                             ?QQQH-  HH      7>7>?HH >>-!>>                                                    
#                           M?Q??QQM   HHHHHHHHHHHHHHQ>!HH.                                                     
#                          H?MH.???HHM HH      >>QMHMMHHQHH                                                     
#                          HHM--???HMMH HH     M>>MM?7! QHHH                                                    
#                          MMM  Q?QHM!M  HH    QM7!  ?HHHMHH!                                                   
#                          !QH .H?QQMHHM HH    MQ .-HHM   :!77>                                                 
#                           QMHHH???HMHHM HH   H.HHH     .>!:77!                                                
#                           .MMMH???QMH>M?MHH?HHH;       .>->; :?                                               
#                            ?Q-;:7??HMHMHHHHHMM         !!M7HHQHHHM                                            
#                             HQ7>77?QMMHHMHHHH          H!>77QQQMHHHHM                                         
#                              >?H77>?HQHH:  >          H?!!M?. .MHQHQQHM                                       
#                                H7>:>H?MM  H          -HQM!>7 . ->?MQH>QH>                                     
#                                 7>!:7H!7             >QHH?!?    7!!;MQH;HM                                    
#                                 77M77?Q7>>?           HHMM!!.;: ;!7  ?QH-HM                                   
#                                 7QMH?77               H?MM:!>;   7:> -H?H?HH                                  
#                                 7!H M .               !?MHH!!> ?MH?Q>?M QHQHM                                 
#                                                        M?HH !>>!HQMH>7.:;QHHHM                                
#                                                         H?HMHMM>?M7> :>  MQHHM7                               
#                                                          M?MM  - .  ..    HHHHM                               
#                                                           M?Q?M ; ;.;;    MQHHM                               
#                                                            M?HQH  : .     M?MHM;                              
#                                                              H?HHHQ  > >  M?MMM                               
#                                                               HH?HHHMMH-MMQ?HHM                               
#                                                                 QH??MHMHM??HMM                                
#                                                                    MHHHHHMHM7                                 

Pathfinder_Race_RNG = random.randrange(len(races.Pathfinder_Race_Dict))
Pathfinder_Class_RNG = random.randrange(len(classes.Pathfinder_Class_Dict))
Pathfinder_Mythic_Path_RNG = random.randrange(len(mythics.Pathfinder_Mythic_Path_Dict))

print("Race is:\t",races.Pathfinder_Race_Dict[Pathfinder_Race_RNG])
print("Class is:\t",classes.Pathfinder_Class_Dict[Pathfinder_Class_RNG])

match Pathfinder_Class_RNG:
    case 0:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Alchemist_Archetypes))
        print("Archetype is:\t", archetypes.Alchemist_Archetypes[Pathfinder_Archetype_RNG])
    case 1:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Arcanist_Archetypes))
        if Pathfinder_Race_RNG != 3:
            while Pathfinder_Archetype_RNG == len(archetypes.Arcanist_Archetypes):
               Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Arcanist_Archetypes))
        print("Archetype is:\t", archetypes.Arcanist_Archetypes[Pathfinder_Archetype_RNG])
    case 2:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Barbarian_Archetypes))
        print("Archetype is:\t", archetypes.Barbarian_Archetypes[Pathfinder_Archetype_RNG])
    case 3:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Bard_Archetypes))
        print("Archetype is:\t", archetypes.Bard_Archetypes[Pathfinder_Archetype_RNG])
    case 4:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Bloodrager_Archetypes))
        if Pathfinder_Race_RNG != 8:
            while Pathfinder_Archetype_RNG == len(archetypes.Bloodrager_Archetypes):
              Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Bloodrager_Archetypes))
        print("Archetype is:\t", archetypes.Bloodrager_Archetypes[Pathfinder_Archetype_RNG])
    case 5:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Cavalier_Archetypes))
        if Pathfinder_Race_RNG != 4:
            while Pathfinder_Archetype_RNG == len(archetypes.Cavalier_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Cavalier_Archetypes))
        print("Archetype is:\t", archetypes.Cavalier_Archetypes[Pathfinder_Archetype_RNG])
    case 6:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Cleric_Archetypes))
        print("Archetype is:\t", archetypes.Cleric_Archetypes[Pathfinder_Archetype_RNG])
    case 7:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Druid_Archetypes))
        print("Archetype is:\t", archetypes.Druid_Archetypes[Pathfinder_Archetype_RNG])
    case 8:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Fighter_Archetypes))
        print("Archetype is:\t", archetypes.Fighter_Archetypes[Pathfinder_Archetype_RNG])
    case 9:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Hunter_Archetypes))
        print("Archetype is:\t", archetypes.Hunter_Archetypes[Pathfinder_Archetype_RNG])
    case 10:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Inquisitor_Archetypes))
        print("Archetype is:\t", archetypes.Inquisitor_Archetypes[Pathfinder_Archetype_RNG])
    case 11:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Kineticist_Archetypes))
        print("Archetype is:\t", archetypes.Kineticist_Archetypes[Pathfinder_Archetype_RNG])
    case 12:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Magus_Archetypes))
        if Pathfinder_Race_RNG != 1:
            while Pathfinder_Archetype_RNG == len(archetypes.Magus_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Magus_Archetypes))
        print("Archetype is:\t", archetypes.Magus_Archetypes[Pathfinder_Archetype_RNG])
    case 13:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Monk_Archetypes))
        if Pathfinder_Race_RNG != 9:
            while Pathfinder_Archetype_RNG == len(archetypes.Monk_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Monk_Archetypes))
        print("Archetype is:\t", archetypes.Monk_Archetypes[Pathfinder_Archetype_RNG])
    case 14:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Oracle_Archetypes))
        if Pathfinder_Race_RNG != 0:
            while Pathfinder_Archetype_RNG == len(archetypes.Oracle_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Oracle_Archetypes))
        print("Archetype is:\t", archetypes.Oracle_Archetypes[Pathfinder_Archetype_RNG])
    case 15:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Paladin_Archetypes))
        if Pathfinder_Race_RNG != 2:
            while Pathfinder_Archetype_RNG == len(archetypes.Paladin_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Paladin_Archetypes))
        print("Archetype is:\t", archetypes.Paladin_Archetypes[Pathfinder_Archetype_RNG])
    case 16:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Ranger_Archetypes))
        print("Archetype is:\t", archetypes.Ranger_Archetypes[Pathfinder_Archetype_RNG])
    case 17:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Rogue_Archetypes))
        if Pathfinder_Race_RNG != 5:
            while Pathfinder_Archetype_RNG == len(archetypes.Rogue_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Rogue_Archetypes))
        print("Archetype is:\t", archetypes.Rogue_Archetypes[Pathfinder_Archetype_RNG])
    case 18:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Shaman_Archetypes))
        if Pathfinder_Race_RNG != 6:
            while Pathfinder_Archetype_RNG == len(archetypes.Shaman_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Shaman_Archetypes))
        print("Archetype is:\t", archetypes.Shaman_Archetypes[Pathfinder_Archetype_RNG])
    case 19:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Skald_Archetypes))
        print("Archetype is:\t", archetypes.Skald_Archetypes[Pathfinder_Archetype_RNG])
    case 20:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Slayer_Archetypes))
        if Pathfinder_Race_RNG != 0:
            while Pathfinder_Archetype_RNG == len(archetypes.Slayer_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Slayer_Archetypes))
        print("Archetype is:\t", archetypes.Slayer_Archetypes[Pathfinder_Archetype_RNG])
    case 21:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Sorcerer_Archetypes))
        if Pathfinder_Race_RNG != 11:
            while Pathfinder_Archetype_RNG == len(archetypes.Sorcerer_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Sorcerer_Archetypes))
        print("Archetype is:\t", archetypes.Sorcerer_Archetypes[Pathfinder_Archetype_RNG])
    case 22:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Warpriest_Archetypes))
        print("Archetype is:\t", archetypes.Warpriest_Archetypes[Pathfinder_Archetype_RNG])
    case 23:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Witch_Archetypes))
        print("Archetype is:\t", archetypes.Witch_Archetypes[Pathfinder_Archetype_RNG])
    case 24:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Wizard_Archetypes))
        if Pathfinder_Race_RNG != 10:
            while Pathfinder_Archetype_RNG == len(archetypes.Wizard_Archetypes):
                Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Wizard_Archetypes))
        print("Archetype is:\t", archetypes.Wizard_Archetypes[Pathfinder_Archetype_RNG])
    case 25:
        Pathfinder_Archetype_RNG = random.randrange(len(archetypes.Shifter_Archetypes))
        print("Archetype is:\t", archetypes.Shifter_Archetypes[Pathfinder_Archetype_RNG])
    case _:
        print("I am Error")


print("Mythic Path is:\t",mythics.Pathfinder_Mythic_Path_Dict[Pathfinder_Mythic_Path_RNG])
input("Press Enter to Exit...")