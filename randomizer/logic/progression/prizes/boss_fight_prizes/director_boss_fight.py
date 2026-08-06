from __future__ import annotations
from randomizer.data.enemies.enemies import (DIRECTOREnemy, POUNDETTEEnemyHenchman)
from randomizer.data.packs.pack_collection import (FORM0260_ONE_DIRECTOR_FOUR_POUNDETTEENEMYHENCHMAN)
from randomizer.data.physical_objects.bosses import (DirectorBattleObject, DirectorLargeObject, DirectorSmallObject, ShovelKnightStatueObject)
from randomizer.data.physical_objects.henchmen import (PoundetteHenchman)
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


class DirectorBossFight(BossFightPrize):
    _text = "Director"
    _formation = FORM0260_ONE_DIRECTOR_FOUR_POUNDETTEENEMYHENCHMAN
    _members = [
        FormationMember(DIRECTOREnemy, 183, 127),
        FormationMember(POUNDETTEEnemyHenchman, 135, 119),
        FormationMember(POUNDETTEEnemyHenchman, 167, 103),
        FormationMember(POUNDETTEEnemyHenchman, 199, 151),
        FormationMember(POUNDETTEEnemyHenchman, 231, 135),
    ]
    _seaside_letter_name_if_seaside_boss = "the Director"
    _seaside_letter_name_if_volcano_boss = "a red-clad smith trudging"
    _seaside_letter_name_if_final_boss = "the Director's minions."

    _npc_models = [DirectorBattleObject, DirectorLargeObject, DirectorSmallObject]
    _statue_npc = ShovelKnightStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=POUNDETTEEnemyHenchman, model=PoundetteHenchman),
    ]
    _character_henchmen = [
        BossFightHenchman(monster=POUNDETTEEnemyHenchman, model=PoundetteHenchman),
        BossFightHenchman(monster=POUNDETTEEnemyHenchman, model=PoundetteHenchman),
        BossFightHenchman(monster=POUNDETTEEnemyHenchman, model=PoundetteHenchman),
        BossFightHenchman(monster=POUNDETTEEnemyHenchman, model=PoundetteHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """DIRECTOR: (Could this day get any\n worse?)[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Figured out the password, did you?[delay_30]\n Don’t get too cocky![delay_30]\n Intruders will be eliminated![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to the Director’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n the DIRECTOR!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """DIRECTOR: I’m afraid I have more\n pressing matters to attend to.\n Depart at once.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """DIRECTOR: Do not waste too much\n time here. Your quest must\n continue.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """DIRECTOR: Any tomfoolery will be\n dealt with by immediate meltdown.\n Get off of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Only the Chief can help you, now.[await]\n I have a Latte with my name on it.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Only the Chief can help you, now.[await]\n I have a Latte with my name on it.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """POUNDETTE: I don’t feel like I’m\n being used to my full potential\n down here.[await][pause] But I don’t mind\n having a break.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """POUNDETTE: I don’t feel like I’m\n being used to my full potential\n down here.[await][pause] but I don’t mind\n having a break.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To Whom It May Concern:[await][page]\n Please conclude all business with `SEASIDE_BOSS` ASAP.[await]\n Your next assignment involves `VOLCANO_BOSS_DESCRIPTION` at the volcano.[await]\n Temporary labor available from `FINAL_BOSS_NAME`[await]\n All changes tenured with immediate effect. Mandatory overtime until the job is complete.[await]\n Direct all inquiries to the Manager.[await][page]\n\n                                   Signed,\n                              the Director[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """POUNDETTE: I don’t feel like I’m\n being used to my full potential\n down here.[await][pause] but I don’t mind\n having a break.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """POUNDETTE: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """POUNDETTE: We’re making a cake\n to look just like the Director![await]""",
        DI2062_APPRENTICE_CHEF: """POUNDETTE: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Director must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """DIRECTOR: I’m afraid you must\n continue searching.[delay] There are\n [0x7024] item(s) remaining.[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """DIRECTOR: I’m afraid you’ve\n overlooked some items in this room.[await]\n Collect them immediately. I will\n not tolerate further delays.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Director is busy right now, so\n he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Director.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """DIRECTOR: I’m afraid there is\n nothing of concern to you in\n this town.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Salutations. How would you like to\n stay in our inn for free today?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Director’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ There’s nothing suspicious going on\n in our town! [delay]Now go on, go to the\n next town![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ No, you can’t see what I’m buying!\n [delay]How rude![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nScram![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There’s some important business\n happening in this shed, so get lost\n and quit trying to interrupt us![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """DIRECTOR: I’m afraid the dojo\n master will be quite a challenge for\n you to beat.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ State your business.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ State your business.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Hammer-this and Meltdown-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Director is busy right now, so\n he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Director.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """POUNDETTE: Well, we lost.\n Time for a break.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """POUNDETTE: You beat the Director!\n Impressive![await]""",
        DI2560_TOWER_HENCHMAN_1: """POUNDETTE: Salutations.[await][pause] Would you\n like to book an appointment with\n the Director?[await][pause]\n ...You want to just barge right\n in?![delay] No way![await]\n Time to teach you some manners![await]""",
        DI2572_TOWER_HENCHMAN_2: """POUNDETTE: The Director doesn’t\n want anyone coming back here.[await]\n So I’m going to have to ask you\n to leave.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """POUNDETTE: Finally, some time to\n rest![await]""",
        DI3073_TOWER_HENCHMAN_3: """\nPOUNDETTE: Let’s see whatcha got![await]""",
    }


__all__ = ["DirectorBossFight"]
