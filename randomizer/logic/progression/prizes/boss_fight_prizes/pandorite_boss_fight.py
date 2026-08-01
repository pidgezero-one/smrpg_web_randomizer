from __future__ import annotations
from randomizer.data.enemies.enemies import (PANDORITEEnemy)
from randomizer.data.packs.pack_collection import (FORM0266_ONE_PANDORITE)
from randomizer.data.physical_objects.bosses import (MimicStatueObject, PandoriteLargeObject, PandoriteSmallObject)
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
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class PandoriteBossFight(BossFightPrize):
    _text = "Pandorite"
    _formation = FORM0266_ONE_PANDORITE
    _members = [
        FormationMember(PANDORITEEnemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a red box sliding about"
    _seaside_letter_name_if_final_boss = "Pandorite's monsters."
    _seaside_letter_name_if_final_boss_remake = "Huhwhat's gremlins."
    _remake_name = "Huhwhat"

    _npc_models = [PandoriteLargeObject, PandoriteSmallObject]
    _statue_npc = MimicStatueObject

    _gender = ("it", "it", "its", "its", "itself")

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PANDORITE: That thing was making\n me sick...[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you cracked the code. I’m\n warning you though, I hate being\n woken up.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Pandorite’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n PANDORITE!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PANDORITE: Whatever... Leave me\n alone so I can go back to sleep.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PANDORITE: I think I like this place\n more than the sewers. It smells\n marginally better.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PANDORITE: I can’t tell if this is\n better or worse without the\n protection of my box.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Here, you can have my...um...[await]\n ’21 Redtail Chardonnay.[delay] It’s fine.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Here, you can have my...um...[await]\n ’21 Redtail Chardonnay.[delay] It’s fine.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,[await][page]\n Someone closed my box, and I floated up here to see your battle with `SEASIDE_BOSS`.[await]\n While looking for rocks, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I think it might be one of `FINAL_BOSS_NAME`[await]\n I’ve got all the rocks in my box so I should sink near the ship. Drop by to see if I made it later.[await][page]\n\n                         Warm Regards,\n                               Pandorite[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Pandorite must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PANDORITE: Sorry, you can’t skip\n getting the last [0x7024] item(s).[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """PANDORITE: Oh, you found all of `MARRYMORE_CHARACTER`’s stuff. Great.[await]\n But you’re missing a few things in this room. How’d you manage to skip that?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Pandorite’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Pandorite.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PANDORITE: There’s not much to do\n around here.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Pandorite...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PANDORITE: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PANDORITE: ...I’m not sure how\n I’m accomplishing this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PANDORITE: ...I’m not sure how\n I’m accomplishing this.[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HUHWHAT: That thing was making\n me sick...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Huhwhat’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n HUHWHAT!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HUHWHAT: Whatever... Leave me\n alone so I can go back to sleep.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HUHWHAT: I think I like this place\n more than the sewers. It smells\n marginally better.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HUHWHAT: I can’t tell if this is\n better or worse without the\n protection of my box.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,[await][page]\n Someone closed my box, and I floated up here to see your battle with `SEASIDE_BOSS`.[await]\n While looking for rocks, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I think it might be one of `FINAL_BOSS_NAME`[await]\n I’ve got all the rocks in my box so I should sink near the ship. Drop by to see if I made it later.[await][page]\n\n                         Warm Regards,\n                                  Huhwhat[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Huhwhat must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HUHWHAT: Sorry, you can’t skip\n getting the last [0x7024] item(s).[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """HUHWHAT: Oh, you found all of `MARRYMORE_CHARACTER`’s stuff. Great.[await]\n But you’re missing a few things in this room. How’d you manage to skip that?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n PHuhwhat’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Huhwhat.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """HUHWHAT: There’s not much to do\n around here.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Huhwhat...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HUHWHAT: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HUHWHAT: ...I’m not sure how\n I’m accomplishing this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HUHWHAT: ...I’m not sure how\n I’m accomplishing this.[await]""",
    }


__all__ = ["PandoriteBossFight"]
