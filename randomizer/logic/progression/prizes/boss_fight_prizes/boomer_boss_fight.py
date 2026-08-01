from __future__ import annotations
from randomizer.data.enemies.enemies import (BOOMEREnemy, HANGINSHYEnemy)
from randomizer.data.packs.pack_collection import (FORM0317_ONE_BOOMER_TWO_HANGINSHY)
from randomizer.data.physical_objects.bosses import (BoomerLargeObject, BoomerOverworldObject, BoomerSmallObject, BoomerStatueObject)
from randomizer.data.variables.battlefield_names import (BF29_BOWSERS_KEEP_CHANDELIERS)
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
    DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT,
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class BoomerBossFight(BossFightPrize):
    _text = "Boomer"
    _formation = FORM0317_ONE_BOOMER_TWO_HANGINSHY
    _members = [
        FormationMember(BOOMEREnemy, 215, 143),
        FormationMember(HANGINSHYEnemy, 66, 115),
        FormationMember(HANGINSHYEnemy, 186, 74),
    ]
    _force_battlefield = BF29_BOWSERS_KEEP_CHANDELIERS
    _seaside_letter_name_if_volcano_boss = "a noble soldier marching"
    _seaside_letter_name_if_final_boss = "Boomer's soldiers."
    _hp_slice_excluded_enemies = [HANGINSHYEnemy, HANGINSHYEnemy]

    _npc_models = [BoomerLargeObject, BoomerOverworldObject, BoomerSmallObject]
    _statue_npc = BoomerStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOMER: I lost fair and square.[await]\n Now it is time for me to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Ahhhhh... So, it’s YOU who solved\n my riddle![delay_30] Now, you’ve got to deal\n with ME![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Boomer’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BOOMER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOMER: I don’t need your\n sympathy! Go on...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOMER: A true soldier knows\n when to accept defeat. You earned\n your victory.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOMER: This is absurd! Get off\n of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Great battle deserves great Sake![await]\n Join me, `MAIN_CHARACTER_NAME`.  Kampai![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Great battle deserves great Sake![await]\n Join me, `MAIN_CHARACTER_NAME`.  Kampai![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ (Origami figures sit in silent tableau:[await][page]\n One figure resembles `VOLCANO_BOSS_DESCRIPTION`[await]. The others appear to be related to `FINAL_BOSS_NAME`[await]\n A haiku lays near the figures: “Stay strong `MAIN_CHARACTER_NAME`[await]\n Show them what discipline means[await]\n Shred them throughly[await][page]\n\n                   Go in peace,\n                         Boomer”)[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like samurai! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Boomer must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOOMER: Ha ha ha![delay_30] So, you found\n [0x7000] item(s) already. Impressive.[await][pause] But\n now you’ve got to find [0x7024] more![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BOOMER: Ha ha ha![await][pause] You found all\n the gear, but your mission isn’t\n over.[await]\n There are still items left in\n this room. A true soldier leaves\n nothing behind![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Boomer’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Boomer.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BOOMER: Ha ha ha![await][pause] So, you’ve\n found our village![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Boomere...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOMER: Ha ha ha! A match\n against the dojo master?!\n This ought to be fun![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Gahahaha! Is it a fight you seek?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Gahahaha! Is it a fight you seek?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Soldier-this and Honor-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOMER: You won fair and square!\n But I won’t make it so easy for you\n next time![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOMER: You won fair and square!\n But I won’t make it so easy for you\n next time![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Boomer’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Boomer.[await]""",
    }


__all__ = ["BoomerBossFight"]
