from __future__ import annotations
from randomizer.data.enemies.enemies import (APPRENTICEEnemyHenchman, BOOSTEREnemy, SNIFITEnemyHenchman)
from randomizer.data.packs.pack_collection import (FORM0271_ONE_BOOSTER_THREE_SNIFITENEMYHENCHMAN)
from randomizer.data.physical_objects.bosses import (BoosterObject, BoosterStatueObject)
from randomizer.data.physical_objects.henchmen import (SnifitHenchman, SpookumHenchman)
from randomizer.data.variables.battle_event_names import (BE0012_DIALOGUE_FROM_BOOSTER_FIGHT)
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
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class BoosterBossFight(BossFightPrize):
    _text = "Booster 1"
    _formation = FORM0271_ONE_BOOSTER_THREE_SNIFITENEMYHENCHMAN
    _force_start_event = BE0012_DIALOGUE_FROM_BOOSTER_FIGHT
    _members = [
        FormationMember(BOOSTEREnemy, 183, 127),
        FormationMember(SNIFITEnemyHenchman, 135, 119),
        FormationMember(SNIFITEnemyHenchman, 151, 143),
        FormationMember(SNIFITEnemyHenchman, 199, 151),
    ]
    _anchor_enemy = BOOSTEREnemy
    # Booster's magic attack is 1, so anchoring that stat to him would multiply his
    # Sniffits' magic attack by 20 (and zero out anything landing in his slot).
    # Magic attack alone anchors to the Sniffit; every other stat stays on Booster.
    _stat_anchor_overrides = {"magic_attack": SNIFITEnemyHenchman}
    _additional_enemies_to_scale = [APPRENTICEEnemyHenchman]
    _seaside_letter_name_if_volcano_boss = "a viking riding trains"
    _seaside_letter_name_if_final_boss = "Booster's frenemies."
    _name = "Booster"

    _npc_models = [BoosterObject]
    _statue_npc = BoosterStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=SNIFITEnemyHenchman, model=SnifitHenchman),
        BossFightHenchman(monster=SNIFITEnemyHenchman, model=SnifitHenchman),
        BossFightHenchman(monster=SNIFITEnemyHenchman, model=SnifitHenchman),
    ]
    _mook_henchmen = [
        BossFightHenchman(monster=APPRENTICEEnemyHenchman, model=SpookumHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOSTER: It’s pretty cozy in here.[await][pause]\n No, you can’t come in![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eh?[delay_30] THAT was my password?![delay_30]\n I’d better fight you, just to be\n sure.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Booster’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BOOSTER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOSTER: I’d love to entertain\n you, but I’m busy watching the\n fish. Come back later.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOSTER: Eh...? My! It’s you\n again![await][page]\n We’re having a lively debate over\n what a “party” is, so you can stay\n if you’d like to contribute.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOSTER: Hm? How’s the view up there?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """SNIFIT 1: There’s a 70% chance the\n drink on the table is actually\n punch.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """SNIFIT 2: Booster can’t find any\n beetles underwater, but he still\n enjoys watching the fish.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Attention `MAIN_CHARACTER_NAME`,[await][page]\n We had an urgent engagement, and regret that we couldn’t stay and play with `SEASIDE_BOSS`.[await]\n While on beetle patrol, #2 saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n Number 3 suggested they might be related to `FINAL_BOSS_NAME` 70% chance. [await]\n We’re riding the Loco Express to the lake of wedding tears.[await]\n Also, Number 1 says there’s no money in the budget for new doors.[await][page]\n\n                                   Booster\n                  Dictated but not read[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """SNIFIT 3: Uh... Do you know where\n we could get some cake down here?[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """SNIFIT 2: Doesn’t this cake\n look just like Booster?[await]""",
        DI2062_APPRENTICE_CHEF: """SNIFIT 3: Uh... I think we should\n have made his mustache bigger.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Booster must have gotten\n lost on his way here.""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nBOOSTER: Found our town, eh?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """SNIFIT 1: Welcome![delay] How would you\n like to stay in our fabulous inn\n for free today?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Booster’s\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """\n You’d better not go near our shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I’m facing a promotion. Do they sell\n anything here that’ll make me look\n more professional?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """SNIFIT 3: Uh... Don’t look in the\n window. [delay]Pretty please.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """SNIFIT 2: There is nothing of\n interest to you in here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOSTER: I wonder if the dojo\n master can shape-shift into a\n Mario doll.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eh? What’d you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Eh? What’d you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Beetle-this and Train-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """SNIFIT 1: Hello there.[await]\n Booster’s busy right now, so we\n can’t let you in.[await]""",
        DI1945_NIMBUS_GUARD: """SNIFIT 2: Please refrain\n from bothering Booster.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Booster’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Booster.[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """SNIFSTER 1: Hello there.[await]\n Booster’s busy right now, so we\n can’t let you in.[await]""",
        DI1945_NIMBUS_GUARD: """SNIFSTER 2: Please refrain\n from bothering Booster.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """APPRENTICE: Oh, dear![delay] We’ve\n failed to keep the intruder away\n from Booster![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """APPRENTICE: Booster’s not happy\n about losing. Please do not jump\n on his head.[await]""",
    }


__all__ = ["BoosterBossFight"]
