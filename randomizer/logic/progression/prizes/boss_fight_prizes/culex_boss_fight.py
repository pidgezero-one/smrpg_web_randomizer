from __future__ import annotations
from randomizer.data.enemies.enemies import (CULEXEnemy, EARTHCRYSTALEnemy, FIRECRYSTALEnemy, WATERCRYSTALEnemy, WINDCRYSTALEnemy)
from randomizer.data.packs.pack_collection import (FORM0322_ONE_CULEX_ONE_FIRECRYSTAL_ONE_WATERCRYSTAL_ONE_EARTHCRYSTAL_ONE_WINDCRYSTAL)
from randomizer.data.physical_objects.bosses import (CulexLargeObject, CulexSmallObject, CulexStatueObject)
from randomizer.data.physical_objects.henchmen import (EarthCrystalHenchman, FireCrystalHenchman, WaterCrystalHenchman, WindCrystalHenchman)
from randomizer.data.variables.battle_event_names import (BE0001_SOLO_WIND_CRYSTAL_APPEARS, BE0011_SOLO_EARTH_CRYSTAL_APPEARS, BE0020_SOLO_WATER_CRYSTAL_APPEARS, BE0076_SOLO_FIRE_CRYSTAL_APPEARS)
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
    DI1786_LETTER_FROM_SHIP_BOSS,
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
    DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
    DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT,
    DI3072_TOWER_HENCHMAN_3_WINDOW,
    DI3073_TOWER_HENCHMAN_3,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class CulexBossFight(BossFightPrize):
    _text = "Culex 1"
    _formation = FORM0322_ONE_CULEX_ONE_FIRECRYSTAL_ONE_WATERCRYSTAL_ONE_EARTHCRYSTAL_ONE_WINDCRYSTAL
    _members = [
        FormationMember(CULEXEnemy, 183, 103),
        FormationMember(FIRECRYSTALEnemy, 135, 103, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 151, 119, hidden_at_start=True),
        FormationMember(EARTHCRYSTALEnemy, 183, 135, hidden_at_start=True),
        FormationMember(WINDCRYSTALEnemy, 215, 143, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "an ethereal knight gliding"
    _seaside_letter_name_if_final_boss = "Culex's crystals."
    _name = "Culex"

    _anchor_enemy = CULEXEnemy
    _hp_slice_excluded_enemies = [
        FIRECRYSTALEnemy,
        WATERCRYSTALEnemy,
        EARTHCRYSTALEnemy,
        WINDCRYSTALEnemy,
    ]

    _henchmen_hidden_at_start = True

    _npc_models = [CulexLargeObject, CulexSmallObject]
    _statue_npc = CulexStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=FIRECRYSTALEnemy, model=FireCrystalHenchman, run_event_at_load=BE0076_SOLO_FIRE_CRYSTAL_APPEARS),
        BossFightHenchman(monster=WATERCRYSTALEnemy, model=WaterCrystalHenchman, run_event_at_load=BE0020_SOLO_WATER_CRYSTAL_APPEARS),
        BossFightHenchman(monster=EARTHCRYSTALEnemy, model=EarthCrystalHenchman, run_event_at_load=BE0011_SOLO_EARTH_CRYSTAL_APPEARS),
        BossFightHenchman(monster=WINDCRYSTALEnemy, model=WindCrystalHenchman, run_event_at_load=BE0001_SOLO_WIND_CRYSTAL_APPEARS),
    ]
    _mook_henchmen = [
        BossFightHenchman(monster=FIRECRYSTALEnemy, model=FireCrystalHenchman, run_event_at_load=BE0076_SOLO_FIRE_CRYSTAL_APPEARS),
        BossFightHenchman(monster=WATERCRYSTALEnemy, model=WaterCrystalHenchman, run_event_at_load=BE0020_SOLO_WATER_CRYSTAL_APPEARS),
        BossFightHenchman(monster=EARTHCRYSTALEnemy, model=EarthCrystalHenchman, run_event_at_load=BE0011_SOLO_EARTH_CRYSTAL_APPEARS),
        BossFightHenchman(monster=WINDCRYSTALEnemy, model=WindCrystalHenchman, run_event_at_load=BE0001_SOLO_WIND_CRYSTAL_APPEARS),
    ]

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
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """WATER CRYSTAL: I guess this is as\n close as I’ll get to being returned\n to Mysidia.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings, honored Warrior.[await][page]\n I have witnessed you do battle with `SEASIDE_BOSS`. I am impressed, but not surprised.[await]\n In my travels of your world, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n The crystals revealed they are `FINAL_BOSS_NAME`[await]\n I know not your path to victory, but challenge awaits you there.[await]\n I must return to the sea, lest the fragile water crystal shatter.[await][page]\n\n                       Fight with honor,\n                                     Culex[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EARTH CRYSTAL: I thought the\n Dark Elf was a bit strange, until\n we came to this world.[await]\n You truly have some characters\n here![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FIRE CRYSTAL: Of course I’m\n miserable! We’re UNDERWATER![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """WIND CRYSTAL: Culex is nice and\n all, but I miss Yang sometimes.[await]""",
        DI2061_HEAD_CHEF: """FIRE CRYSTAL: We needed a lot of\n heat to bake a cake of this size.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Culex must have gotten\n lost on his way here.""",
        DI2062_APPRENTICE_CHEF: """WATER CRYSTAL: We must shape\n this confection to resemble Culex.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CULEX: You must retrieve [0x7024] more\n item(s) before we may proceed.[await]\n Godspeed, champion knight![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """CULEX: It would be wise of you to\n search this room for more\n equipment.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Culex is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Culex.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nCULEX: Good day.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome to our inn.[await]\n We are offering a competitive price\n of zero coins per night.[await]\n Will you be staying tonight?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Culex’s\n house up on the hill yet?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n[center]This area is off-limits.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ This door is a... uh... portal to another dimension! We can’t let you fall into it.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CULEX: It will be quite difficult to\n claim victory over the dojo master.\n I wish you luck.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """WATER CRYSTAL: This area is\n off-limits.[await]""",
        DI1945_NIMBUS_GUARD: """EARTH CRYSTAL: Are you sure you\n want to mess with a water crystal\n in a cloud kingdom?[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: '''  You will enter combat against me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]'''
        }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """CRYSTAL: Proceed forth. Culex\n awaits you.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """CRYSTAL: Well met! You have\n satisfied Culex’s hunger for a\n true challenge.[await]""",
        DI2560_TOWER_HENCHMAN_1: """FIRE CRYSTAL: Greetings.[await][pause] Culex\n is making preparations to head\n back to his home world.[await][pause] He’s\n busy right now.[await][page]\n Please come back later...\n [delay]unless you want to get hurt![await]""",
        DI2572_TOWER_HENCHMAN_2: """WATER CRYSTAL: You are not going\n to find what you’re seeking back\n here.[delay] Stay out.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EARTH CRYSTAL: Wind Crystal\n really should have been the one\n standing guard all the way up here.[await]""",
        DI3073_TOWER_HENCHMAN_3: """EARTH CRYSTAL: Stand back!\n I might know Sandstorm![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Culex is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Culex.[await]""",
    }


__all__ = ["CulexBossFight"]
