from __future__ import annotations
from randomizer.data.enemies.enemies import (CULEX3DEnemy, FIRECRYS3DEnemy)
from randomizer.data.packs.pack_collection import (FORM0096_ONE_CULEX3D_ONE_FIRECRYS3D_ONE_WATERCRYS3D_ONE_EARTHCRYS3D_ONE_WINDCRYS3D)
from randomizer.data.physical_objects.bosses import (Culex3DSmallObject, CulexStatueObject)
from randomizer.data.variables.battlefield_names import (BF47_CULEX)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1660_SHIP_PASSWORD_COMPLETE,
    DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
    DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
    DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
    DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
    DI1781_SHIP_BOSS_JUMP_ON_HEAD,
    DI1782_SHIP_BOSS_DRINK,
    DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
    DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1,
    DI1786_LETTER_FROM_SHIP_BOSS,
    DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
    DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4,
    DI2023_SHIP_BOSS_2_DRINK,
    DI2061_HEAD_CHEF,
    DI2180_CHAPEL_NPC,
    DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
    DI2560_TOWER_HENCHMAN_1,
    DI2572_TOWER_HENCHMAN_2,
    DI2830_SEASIDE_BOSS_WELCOMES_YOU,
    DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
    DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
    DI3057_MONSTRO_SUPERBOSS_PROMPT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class Culex3DBossFight(BossFightPrize):
    _text = "Culex 2"
    _formation = FORM0096_ONE_CULEX3D_ONE_FIRECRYS3D_ONE_WATERCRYS3D_ONE_EARTHCRYS3D_ONE_WINDCRYS3D
    _members = [
        FormationMember(CULEX3DEnemy, 183, 103),
        FormationMember(FIRECRYS3DEnemy, 135, 103, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 151, 119, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 183, 135, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 215, 143, hidden_at_start=True),
    ]
    #_force_start_event = BE0077_CULEX_3D
    _anchor_enemy = CULEX3DEnemy

    _seaside_letter_name_if_volcano_boss = "an ethereal knight gliding"
    _seaside_letter_name_if_final_boss = "Culex's crystals."
    _name = "Culex"

    _npc_models = [Culex3DSmallObject]
    _statue_npc = CulexStatueObject

    _force_battlefield = BF47_CULEX


    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CULEX: Please do not attempt to\n crack this egg again.[await][page]\n It will not give you 34,000 experience points.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ You have passed the first test.\n But you’re not finished yet!\n Please enter.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Culex’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped CULEX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CULEX: This world truly is\n uninhabitable for me and my kind...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CULEX: Greetings.[delay] It is good to make your acquaintance once again.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CULEX: This is not the encounter I expected when I came to visit this world.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ How droll, my crystals shattered.[await]\n I’ve only Bacchus Wine remaining.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ How droll, my crystals shattered.[await]\n I’ve only Bacchus Wine remaining.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings, honored Warrior.[await][page]\n I have witnessed you do battle with `SEASIDE_BOSS`. I am impressed, but not surprised.[await]\n In my travels of your world, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n The crystals revealed they are `FINAL_BOSS_NAME`[await]\n I know not your path to victory, but challenge awaits you there.[await]\n I must return to the sea, lest the fragile water crystal shatter.[await][page]\n\n                       Fight with honor,\n                                     Culex[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like demon! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Culex must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CULEX: You must retrieve [0x7024] more\n item(s) before we may proceed.[await]\n Godspeed, champion knight![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """CULEX: It would be wise of you to\n search this room for more\n equipment.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nCULEX: Good day.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Culex...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CULEX: It will be quite difficult to\n claim victory over the dojo master.\n I wish you luck.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: ''' You will enter combat against me\n in 3D?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]'''
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Culex is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Culex.[await]""",
    }


__all__ = ["Culex3DBossFight"]
