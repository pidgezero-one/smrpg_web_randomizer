from __future__ import annotations
from randomizer.data.enemies.enemies import (CLERKEnemy, MADMALLETEnemyHenchman)
from randomizer.data.packs.pack_collection import (FORM0258_ONE_CLERK_TWO_MADMALLETENEMYHENCHMAN)
from randomizer.data.physical_objects.bosses import (ClerkBattleObject, ClerkLargeObject, ClerkSmallObject, ShovelKnightStatueObject)
from randomizer.data.physical_objects.henchmen import (MadMalletHenchman)
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


class ClerkBossFight(BossFightPrize):
    _text = "Clerk"
    _formation = FORM0258_ONE_CLERK_TWO_MADMALLETENEMYHENCHMAN
    _members = [
        FormationMember(CLERKEnemy, 199, 119),
        FormationMember(MADMALLETEnemyHenchman, 135, 119),
        FormationMember(MADMALLETEnemyHenchman, 199, 151),
    ]
    _seaside_letter_name_if_seaside_boss = "the Clerk"
    _seaside_letter_name_if_volcano_boss = "a yellow-clad smith trudging"
    _seaside_letter_name_if_final_boss = "the Clerk's minions."

    _npc_models = [ClerkBattleObject, ClerkLargeObject, ClerkSmallObject]
    _statue_npc = ShovelKnightStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=MADMALLETEnemyHenchman, model=MadMalletHenchman),
    ]
    _character_henchmen = [
        BossFightHenchman(monster=MADMALLETEnemyHenchman, model=MadMalletHenchman),
        BossFightHenchman(monster=MADMALLETEnemyHenchman, model=MadMalletHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CLERK: I’m going to sleep for 10\n years.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Sorry, you may have figured out the\n password, but I can’t allow you\n through without a fight.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to the Clerk’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n the CLERK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CLERK: I don’t get paid nearly\n enough to get whooped that\n badly...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CLERK: So, you’ve come back! I\n hope your journey is staying on\n schedule![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CLERK: What do you think you’re\n doing?![await]""",
        DI1782_SHIP_BOSS_DRINK: """ You’ll have to take this up with the[await]\n Manager.  I’M having an Espresso.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ You’ll have to take this up with the[await]\n Manager.  I’M having an Espresso.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """MAD MALLET: To be honest, I hate\n fighting alone. I’ll run away if I’m\n the last one left in a battle.[await]\n It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """MAD MALLET: To be honest, I hate\n fighting alone. I’ll run away if I’m\n the last one left in a battle.[await]\n It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`,[await][page]\n When you can, I need a report on your the results of your battle with `SEASIDE_BOSS`.[await]\n On company retreat, I met `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n Mad Mallet saw them having drinks with `FINAL_BOSS_NAME`[await]\n I’ve got to get back to work. I spent my break writing this.[await]\n If you happen to return to the ship, could you bring me a Pick Me Up?[await][page]\n\n                                   Thanks,\n                                 the Clerk[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """MAD MALLET: To be honest, I hate\n fighting alone. I’ll run away if I’m\n the last one left in a battle.[await]\n It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """MAD MALLET: Hop on the\n trampoline in the next room. It’ll\n take you outside.[await]""",
        DI2061_HEAD_CHEF: """MAD MALLET: We’re making a cake\n to look just like the Clerk![await]""",
        DI2062_APPRENTICE_CHEF: """MAD MALLET: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Clerk must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CLERK: Whatcha got? [0x7000] item(s)?\n At this rate, you should find the\n last [0x7024] in no time![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """CLERK: Good work finding all the\n gear.[await]\n But there are still some\n items in this room you need to\n grab. Stay on schedule![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Clerk is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Clerk.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CLERK: Not much happens in this\n quiet and completely unsuspicious\n town.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome.[delay] Would you like to stay\n here for free?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Clerk’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """[center]\nDon’t go snooping around our town![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """[center]\nI’m just shopping here![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """[center]\nGet lost![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hey buddy, why don’t you go snoop\n around some other houses instead?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CLERK: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you here for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Are you here for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Hammer-this and Puffball-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CLERK: If anyone asks, I’m on\n break![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CLERK: If anyone asks, I’m on\n break![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Clerk is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Clerk.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """MAD MALLET: You trashed us!\n Go on to the Clerk’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """MAD MALLET: Whoa... No one’s\n beaten the Clerk in 10 years![await]""",
        DI2560_TOWER_HENCHMAN_1: """MAD MALLET: Welcome.[await][pause] It’s the\n Clerk’s day off, so he’s not taking\n visitors today.[await][page]\n ...But if you insist, I’ll have to\n keep you out myself![await]""",
        DI2572_TOWER_HENCHMAN_2: """MAD MALLET: Listen, the Clerk\n doesn’t get paid enough to deal\n with you.[await][page]\n  I certainly don’t either, but I’m\n having a bad day![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """MAD MALLET: Wow! I can see\n Nimbus Land from here![await]""",
        DI3073_TOWER_HENCHMAN_3: """MAD MALLET: I’m gonna THRASH\n ya![await]""",
    }


__all__ = ["ClerkBossFight"]
