from __future__ import annotations
from randomizer.data.enemies.enemies import (COUNTDOWNEnemy, DINGALINGEnemy)
from randomizer.data.packs.pack_collection import (FORM0284_ONE_COUNTDOWN_TWO_DINGALING)
from randomizer.data.physical_objects.bosses import (CountDownGridplaneObject, CountDownStatueObject)
from randomizer.data.physical_objects.henchmen import (DingalingHenchman)
from randomizer.data.variables.battlefield_names import (BF18_SMITHY_FACTORY_COUNT_DOWNS_PAD)
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


class CountdownBossFight(BossFightPrize):
    _text = "Count Down"
    _formation = FORM0284_ONE_COUNTDOWN_TWO_DINGALING
    _members = [
        FormationMember(COUNTDOWNEnemy, 150, 93),
        FormationMember(DINGALINGEnemy, 158, 52),
        FormationMember(DINGALINGEnemy, 194, 67),
    ]
    _force_battlefield = BF18_SMITHY_FACTORY_COUNT_DOWNS_PAD
    _anchor = COUNTDOWNEnemy

    _seaside_letter_name_if_seaside_boss = "the Clock"
    _seaside_letter_name_if_volcano_boss = "a noisy clock winding"
    _seaside_letter_name_if_final_boss = "Count Down's friends."

    _npc_models = [CountDownGridplaneObject]
    _statue_npc = CountDownStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=DINGALINGEnemy, model=DingalingHenchman),
    ]

    _gender = ("it", "it", "its", "its", "itself")

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """COUNT DOWN: Sometimes, even an\n alarm clock needs to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ This is not good![delay_30]\n He figured out the password![delay_30]\n ...We better do something![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Count Down’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n COUNT DOWN!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """COUNT DOWN: ...What time is it?\n Time for you to leave![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """COUNT DOWN: What are you still\n doing around here? Taking a break,\n huh?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """[center]\nCOUNT DOWN: This is not good![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Ahh, fresh squeezed Orange Juice-[await]\n The second best way to wake up![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Ahh, fresh squeezed Orange Juice-[await]\n The second best way to wake up![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """DING-A-LING: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """DING-A-LING: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """DING-A-LING: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """DING-A-LING: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ WAKE UP CALL FOR `MAIN_CHARACTER_NAME`!![await][page]\n YOU’RE LATE DEFEATING `SEASIDE_BOSS`!![await]\n NEWSFLASH: `VOLCANO_BOSS_DESCRIPTION` SPOTTED NEAR THE VOLCANO!![await]\n DING-A-LING SOURCES LINK TO `FINAL_BOSS_NAME`[await]\n TIME WAITS FOR NO ONE!![await]\n BETTER NAIL THAT MACK SKIP, ROCK CANDY MANIP, BLOCK CLIP, BACK TO SUNKEN SHIP, YIP!![await][page]\n\n Alarm off  <<<        >>>  Snooze\n                              Count Down[await]""",
        DI2061_HEAD_CHEF: """DING-A-LING: I guess it is a little\n weird to make a cake that looks\n like a clock with no body.[await]""",
        DI2062_APPRENTICE_CHEF: """DING-A-LING: Are you impressed by\n how well we can bake without\n having any hands?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Down must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """COUNT DOWN: You’ve only got\n [0x7000] item(s)! You’re missing [0x7024]![await]\n You better do something![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """COUNT DOWN: Uh-oh! You found all\n the gear, but you’re not done yet![await]\n There are still items in this room!\n You better do something![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Count Down’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Count Down.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """COUNT DOWN: There’s nothing to\n do here![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Our inn is free![await][pause] Why?[delay_30] Uh...[delay]\n I’m not sure.[delay_30] Anyway,[delay] do you\n want to stay?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Count Down’s\n house up on the hill yet?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nThis is off-limits! Scram![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nGet outta here! Beat it![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """COUNT DOWN: The dojo master will\n be tough to beat![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Uh-oh! Are you looking for\n trouble?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Uh-oh! Are you looking for\n trouble?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n The guy next door never seems\n to shut his alarm clock off.[await][page]\n I’d like to go over and give him a\n piece of my mind, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Count Down’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Count Down.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """RING-A-DING: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """RING-A-DING: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ WAKE UP CALL FOR `MAIN_CHARACTER_NAME`!![await][page]\n YOU’RE LATE DEFEATING `SEASIDE_BOSS`!![await]\n NEWSFLASH: `VOLCANO_BOSS_DESCRIPTION` SPOTTED NEAR THE VOLCANO!![await]\n RING-A-DING SOURCES LINK TO `FINAL_BOSS_NAME`[await]\n TIME WAITS FOR NO ONE!![await]\n BETTER NAIL THAT MACK SKIP, ROCK CANDY MANIP, BLOCK CLIP, BACK TO SUNKEN SHIP, YIP!![await][page]\n\n Alarm off  <<<        >>>  Snooze\n                              Count Down[await]""",
        DI2061_HEAD_CHEF: """RING-A-DING: I guess it is a little\n weird to make a cake that looks\n like a clock with no body.[await]""",
        DI2062_APPRENTICE_CHEF: """RING-A-DING: Are you impressed by\n how well we can bake without\n having any hands?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """DING-A-LING: We failed to stop\n you. Go ahead into Count Down’s\n room![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """DING-A-LING: You beat Count Down!\n We didn’t see that coming![await]""",
        DI2560_TOWER_HENCHMAN_1: """DING-A-LING: `MAIN_CHARACTER_NAME`’s HERE![await][pause][delay_30]\n I’d better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """DING-A-LING: You won’t find\n Count Down back here![await]\n Leave us alone![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """DING-A-LING: Man...[delay_15] I’m tired.[await]\n Even alarm bells get tired\n sometimes.[await]""",
        DI3073_TOWER_HENCHMAN_3: """DING-A-LING: Back off![delay_15] I know\n Fear Roulette and I’m not afraid\n to use it![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """RING-A-DING: We failed to stop\n you. Go ahead into Count Down’s\n room![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """RING-A-DING: You beat Count Down!\n We didn’t see that coming![await]""",
        DI2560_TOWER_HENCHMAN_1: """RING-A-DING: `MAIN_CHARACTER_NAME`’s HERE![await][pause][delay_30]\n I’d better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """RING-A-DING: You won’t find\n Count Down back here![await]\n Leave us alone![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """RING-A-DING: Man...[delay_15] I’m tired.[await]\n Even alarm bells get tired\n sometimes.[await]""",
        DI3073_TOWER_HENCHMAN_3: """RING-A-DING: Back off![delay_15] I know\n Fear Roulette and I’m not afraid\n to use it![await]""",
    }


__all__ = ["CountdownBossFight"]
