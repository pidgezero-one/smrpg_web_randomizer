from __future__ import annotations
from randomizer.data.enemies.enemies import (CZARDRAGONEnemy, HELIOEnemy, PYROSPHEREEnemyHenchman, ZOMBONEEnemy)
from randomizer.data.packs.pack_collection import (FORM0282_ONE_CZARDRAGON_ONE_ZOMBONE_FOUR_HELIO)
from randomizer.data.physical_objects.bosses import (CzarDragonLargeObject, CzarDragonMediumObject, CzarDragonSmallObject, CzarStatueObject)
from randomizer.data.physical_objects.henchmen import (HelioHenchman, SparkyHenchman)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1120_NIMBUS_BIRD_GUARD,
    DI1660_SHIP_PASSWORD_COMPLETE,
    DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
    DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
    DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
    DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
    DI1781_SHIP_BOSS_JUMP_ON_HEAD,
    DI1782_SHIP_BOSS_DRINK,
    DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
    DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1,
    DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
    DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4,
    DI1945_NIMBUS_GUARD,
    DI2023_SHIP_BOSS_2_DRINK,
    DI2061_HEAD_CHEF,
    DI2062_APPRENTICE_CHEF,
    DI2180_CHAPEL_NPC,
    DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
    DI2560_TOWER_HENCHMAN_1,
    DI2572_TOWER_HENCHMAN_2,
    DI2830_SEASIDE_BOSS_WELCOMES_YOU,
    DI2832_OCCUPIED_SEASIDE_INNKEEPER,
    DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING,
    DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED,
    DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
    DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED,
    DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER,
    DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
    DI3057_MONSTRO_SUPERBOSS_PROMPT,
    DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT,
    DI3072_TOWER_HENCHMAN_3_WINDOW,
    DI3073_TOWER_HENCHMAN_3,
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class CzarDragonBossFight(BossFightPrize):
    _text = "Czar Dragon"
    _formation = FORM0282_ONE_CZARDRAGON_ONE_ZOMBONE_FOUR_HELIO
    _members = [
        FormationMember(CZARDRAGONEnemy, 183, 143),
        FormationMember(ZOMBONEEnemy, 183, 143, hidden_at_start=True),
        FormationMember(HELIOEnemy, 167, 119, hidden_at_start=True),
        FormationMember(HELIOEnemy, 135, 135, hidden_at_start=True),
        FormationMember(HELIOEnemy, 199, 167, hidden_at_start=True),
        FormationMember(HELIOEnemy, 231, 151, hidden_at_start=True),
    ]
    # Anchor is the average of Czar Dragon and Zombone (excluding Helios)
    _anchor_enemy = [CZARDRAGONEnemy, ZOMBONEEnemy]
    _scaling_excluded_enemies = [HELIOEnemy, HELIOEnemy, HELIOEnemy, HELIOEnemy]
    _additional_enemies_to_scale = [PYROSPHEREEnemyHenchman]

    _seaside_letter_name_if_seaside_boss = "the Dragon"
    _seaside_letter_name_if_volcano_boss = "a huge dragon blazing"
    _seaside_letter_name_if_final_boss = "the Czar Dragon's spawn."
    _seaside_letter_name_if_seaside_boss_canon = "Blargg's spawn."

    _npc_models = [CzarDragonLargeObject, CzarDragonMediumObject, CzarDragonSmallObject]
    _statue_npc = CzarStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=PYROSPHEREEnemyHenchman, model=SparkyHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=HELIOEnemy, model=HelioHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """[center]\nCZAR DRAGON: BLARRGGGG[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """[center]\nBLARRGGGG[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to the Czar Dragon’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n the CZAR DRAGON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nCZAR DRAGON: BLARRGGGG[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """[center]\nCZAR DRAGON: BLARRGGGG[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """[center]\nCZAR DRAGON: BLARRGGGG[await]""",
        DI1782_SHIP_BOSS_DRINK: """ FIIIIIIIRRRRREEEEBAAAALLLLLLLL[await]\n WHISSSSSSSSSKEEEEEEEEEEEEY!!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ FIIIIIIIRRRRREEEEBAAAALLLLLLLL[await]\n WHISSSSSSSSSKEEEEEEEEEEEEY!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: "[center]\n••••••[await]",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: "[center]\n••••••[await]",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: "[center]\n••••••[await]",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: "[center]\n••••••[await]",
        DI2061_HEAD_CHEF: "[center]\n••••••[await]",
        DI2062_APPRENTICE_CHEF: "[center]\n••••••[await]",
        DI2180_CHAPEL_NPC: """ Reverend Dragon must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """\n    CZAR DRAGON: BLARRGGGG[await][page]\n (He means to say you are missing\n [0x7024] more items.)[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """\n    CZAR DRAGON: BLARRGGGGRRGGG[await][page]\n (He means to say you should grab\n the last few items in this room\n before proceeding.)[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Czar Dragon is busy right now,\n so he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Czar Dragon.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nCZAR DRAGON: BLAAARRRGGGG[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ (Stay in the inn for free?)[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: "[center]\n••••••[await]",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: "[center]\n••••••[await]",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: "[center]\n••••••[await]",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: "[center]\n••••••[await]",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "[center]\n••••••[await]",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: "[center]\n••••••[await]",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: "[center]\n••••••[await]",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: "[center]\n••••••[await]",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: "[center]\nCZAR DRAGON: BLAAARRRGGGG[await]",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: "CZAR DRAGON:\n[center]BLAAARRRGGGG\n  [select] (I agree, let’s fight)\n  [select] (Uh...)[await]",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: "CZAR DRAGON:\n[center]BLAAARRRGGGG\n  [select] (I agree, let’s fight)\n  [select] (Uh...)[await]",
        DI3338_MONSTRO_SUPERBOSS_HINT: " It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always yelling about\n BLARRRRG-this and\n BLAHGAHRGGH-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: "[center]\nCZAR DRAGON: BLAAARRRGGGG[await]",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: "[center]\nCZAR DRAGON: BLAAARRRGGGG[await]",
        DI1120_NIMBUS_BIRD_GUARD: "[center]\n••••••[await]",
        DI1945_NIMBUS_GUARD: "[center]\n••••••[await]",
    }
    _dialog_replacements_canon = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """[center]\nBLARGG: BLARRGGGG[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Blargg’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n BLARGG!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nBLARGG: BLARRGGGG[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """[center]\nBLARGG: BLARRGGGG[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """[center]\nBLARGG: BLARRGGGG[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Blargg must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """\n    BLARGG: BLARRGGGG[await][page]\n (He means to say you are missing\n [0x7024] more items.)[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """\n    BLARGG: BLARRGGGGRRGGG[await][page]\n (He means to say you should grab\n the last few items in this room\n before proceeding.)[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Blargg is busy right now,\n so he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Blargg.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nBLARGG: BLAAARRRGGGG[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: "[center]\nBLARGG: BLAAARRRGGGG[await]",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: "BLARGG:\n[center]BLAAARRRGGGG\n  [select] (I agree, let’s fight)\n  [select] (Uh...)[await]",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: "BLARGG:\n[center]BLAAARRRGGGG\n  [select] (I agree, let’s fight)\n  [select] (Uh...)[await]",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: "[center]\nBLARGG: BLAAARRRGGGG[await]",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: "[center]\nBLARGG: BLAAARRRGGGG[await]",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Czar Dragon is busy right now,\n so he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Czar Dragon.[await]""",
    }
    _dialog_replacements_canon_and_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Blargg is busy right now,\n so he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Blargg.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI2560_TOWER_HENCHMAN_1: "[center]\n••••••[await]",
        DI2572_TOWER_HENCHMAN_2: "[center]\n••••••[await]",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: "[center]\n••••••[await]",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: "[center]\n••••••[await]",
        DI3072_TOWER_HENCHMAN_3_WINDOW: "[center]\n••••••[await]",
        DI3073_TOWER_HENCHMAN_3: "[center]\n••••••[await]",
    }


__all__ = ["CzarDragonBossFight"]
