from __future__ import annotations
from randomizer.data.enemies.enemies import (MANAGEREnemy, POUNDEREnemyHenchman)
from randomizer.data.packs.pack_collection import (FORM0259_ONE_MANAGER_THREE_POUNDERENEMYHENCHMAN)
from randomizer.data.physical_objects.bosses import (ManagerBattleObject, ManagerLargeObject, ManagerSmallObject, ShovelKnightStatueObject)
from randomizer.data.physical_objects.henchmen import (PounderHenchman)
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


class ManagerBossFight(BossFightPrize):
    _text = "Manager"
    _formation = FORM0259_ONE_MANAGER_THREE_POUNDERENEMYHENCHMAN
    _members = [
        FormationMember(MANAGEREnemy, 199, 119),
        FormationMember(POUNDEREnemyHenchman, 151, 111),
        FormationMember(POUNDEREnemyHenchman, 167, 135),
        FormationMember(POUNDEREnemyHenchman, 215, 143),
    ]
    _seaside_letter_name_if_seaside_boss = "the Manager"
    _seaside_letter_name_if_volcano_boss = "a blue-clad smith trudging"
    _seaside_letter_name_if_final_boss = "the Manager's minions."

    _npc_models = [ManagerBattleObject, ManagerLargeObject, ManagerSmallObject]
    _statue_npc = ShovelKnightStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=POUNDEREnemyHenchman, model=PounderHenchman),
    ]
    _character_henchmen = [
        BossFightHenchman(monster=POUNDEREnemyHenchman, model=PounderHenchman),
        BossFightHenchman(monster=POUNDEREnemyHenchman, model=PounderHenchman),
        BossFightHenchman(monster=POUNDEREnemyHenchman, model=PounderHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MANAGER: I’m going to sleep for 25 years.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Who gave you the password?!\n You’re gonna pay for this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to the Manager’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n the MANAGER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """MANAGER: Why don’t you just jump\n on out of here?![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MANAGER: Oh, you’ve returned.\n Good work so far.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MANAGER: Get off of my head\n before I make you take the longest\n jump of your life![await]""",
        DI1782_SHIP_BOSS_DRINK: """ DON’T bother the Director with this.[await]\n Just, drink my Cappuccino. Happy?[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ DON’T bother the Director with this.[await]\n Just, drink my Cappuccino. Happy?[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,[await][page]\n Have you taken care of `SEASIDE_BOSS` yet?[await]\n There’s a report on my desk about `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They’re a priority client of `FINAL_BOSS_NAME`[await]\n Take care of them, pronto. All vacation time rescinded until it’s done. I expect regular updates.[await][page]\n\n      Make it happen or you’re fired.\n                             The Manager[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """POUNDER: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """POUNDER: We’re making a cake\n to look just like the Manager![await]""",
        DI2062_APPRENTICE_CHEF: """POUNDER: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Manager must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MANAGER: Heh heh heh.[delay] Good work.[await]\n You just need [0x7024] more item(s).[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """MANAGER: You found all the gear.\n Good.[await]\n But there are still items in\n this room. Don’t disturb me until\n they’re collected![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Manager is busy right now, so\n he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Manager.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """MANAGER: Come to invade our\n town, have you?[await][pause] No need, there’s\n nothing of interest here, I swear![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Good day.[delay] We’re offering free\n reservations today. Would you like\n to stay?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Manager’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ If you’re gonna snoop around,\n [delay]just don’t do it near the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Hey buddy, I’m just trying to shop\n here. Why don’t you mind your own\n business?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nDon’t bother us![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nCan’t you see we’re busy?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MANAGER: You think you can beat\n the dojo master?![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Yes?[await][pause] What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Yes?[await][pause] What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Hammer-this and Schedule-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MANAGER: Don’t interrupt me while\n I’m training![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MANAGER: Don’t interrupt me while\n I’m training![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Manager is busy right now, so\n he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Manager.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """POUNDER: We lost, but we made\n the Manager proud![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """POUNDER: Wow! The Manager’s\n been here 25 years, and you just\n dethroned him![await]""",
        DI2560_TOWER_HENCHMAN_1: """POUNDER: Good day.[await][pause] The Manager\n is busy today and will not be\n seeing any guests.[await][pause]\n If you try to force your way in,\n I’ll have to deal with you![await]""",
        DI2572_TOWER_HENCHMAN_2: """POUNDER: Stay outta our hair![await]\n [delay]...Huh? [delay]“You don’t have hair”?[await][pause]\n That’s it, you’re asking for it![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """POUNDER: Man, I need a break. This\n job is tiring.[await]""",
        DI3073_TOWER_HENCHMAN_3: """POUNDER: Bullet Bill production is\n on schedule! Don’t get in my way![await]""",
    }


__all__ = ["ManagerBossFight"]
