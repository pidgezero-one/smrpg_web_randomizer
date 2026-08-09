from __future__ import annotations
from randomizer.data.enemies.enemies import (BOOSTERDUMMY, BOOSTEREnemy2, SNIFIT2Enemy)
from randomizer.data.packs.pack_collection import (FORM0123_ONE_BOOSTERENEMY2_THREE_SNIFIT2_ONE_BOOSTERDUMMY)
from randomizer.data.physical_objects.bosses import (Booster2SmallObject, BoosterStatueObject)
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
)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class Booster2BossFight(BossFightPrize):
    _text = "Booster 2"
    _formation = FORM0123_ONE_BOOSTERENEMY2_THREE_SNIFIT2_ONE_BOOSTERDUMMY
    _members = [
        FormationMember(BOOSTEREnemy2, 184, 116),
        FormationMember(SNIFIT2Enemy, 156, 132),
        FormationMember(SNIFIT2Enemy, 143, 104),
        FormationMember(SNIFIT2Enemy, 212, 138),
        FormationMember(BOOSTERDUMMY, 0, 0),
    ]
    _anchor_enemy = BOOSTEREnemy2
    _stat_anchor_overrides = {"magic_attack": SNIFIT2Enemy}

    _seaside_letter_name_if_volcano_boss = "a viking riding trains"
    _seaside_letter_name_if_final_boss = "Booster's frenemies."
    _name = "Booster"
    _scaling_excluded_enemies = [BOOSTERDUMMY]
    _hp_slice_excluded_enemies = [
        BOOSTERDUMMY,
        SNIFIT2Enemy,
        SNIFIT2Enemy,
        SNIFIT2Enemy
    ]

    _npc_models = [Booster2SmallObject]
    _statue_npc = BoosterStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOSTER: It’s pretty cozy in here.[await][pause]\n No, you can’t come in![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eh?[delay_30] THAT was my password?![delay_30]\n I’d better fight you, just to be\n sure.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Booster’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BOOSTER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOSTER: I’d love to entertain\n you, but I’m busy watching the\n fish. Come back later.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOSTER: Eh...? My! It’s you\n again![await][page]\n  We’re having a heated debate over\n what a “party” is, so you can stay\n if you’d like to contribute.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOSTER: Hm? How’s the view up there?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Attention `MAIN_CHARACTER_NAME`,[await][page]\n We had an urgent engagement, and regret that we couldn’t stay and play with `SEASIDE_BOSS`.[await]\n While on beetle patrol, #2 saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n Number 3 suggested they might be related to `FINAL_BOSS_NAME` 70% chance. [await]\n We’re riding the Loco Express to the lake of wedding tears.[await]\n Also, Number 1 says there’s no money in the budget for new doors.[await][page]\n\n                                   Booster\n                  Dictated but not read[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like stinky man! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Booster must have gotten\n lost on his way here.""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nBOOSTER: Found our town, eh?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Booster...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOSTER: I wonder if the dojo\n master can shape-shift into a\n Mario doll.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eh? What’d you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Eh? What’d you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Beetle-this and Train-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Booster’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Booster.[await]""",
    }


__all__ = ["Booster2BossFight"]
