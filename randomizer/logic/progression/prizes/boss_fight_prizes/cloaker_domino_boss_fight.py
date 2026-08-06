from __future__ import annotations
from randomizer.data.enemies.enemies import (CLOAKEREnemy, CLOAKEREnemy2, DOMINOEnemy, DOMINOEnemy2, EARTHLINKEnemy, MADADDEREnemy)
from randomizer.data.packs.pack_collection import (FORM0294_ONE_CLOAKER_ONE_DOMINO_ONE_MADADDER)
from randomizer.data.physical_objects.bosses import (DominoLargeObject, DominoSmallObject, DominoStatueObject)
from randomizer.data.variables.battle_event_names import (BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION)
from randomizer.data.variables.battlefield_names import (BF40_SMITHY_FACTORY_DOMINO_CLOAKERS_PAD)
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


class CloakerDominoBossFight(BossFightPrize):
    _text = "Cloaker & Domino"
    _formation = FORM0294_ONE_CLOAKER_ONE_DOMINO_ONE_MADADDER
    _members = [
        FormationMember(CLOAKEREnemy, 151, 111),
        FormationMember(DOMINOEnemy, 215, 159),
        FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
    ]
    _anchor_enemy = [CLOAKEREnemy, DOMINOEnemy]
    _additional_enemies_to_scale = [EARTHLINKEnemy, CLOAKEREnemy2, DOMINOEnemy2]
    _extra_hp_enemies = [EARTHLINKEnemy]
    # You only fight 2 of the 4 enemies (Cloaker+EarthLink OR Domino+MadAdder)
    _location_hp_multiplier = 0.5

    _force_battlefield = BF40_SMITHY_FACTORY_DOMINO_CLOAKERS_PAD
    _force_start_event = BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION
    _seaside_letter_name_if_seaside_boss = "the Snake"
    _seaside_letter_name_if_volcano_boss = "a snake slithering around"
    _seaside_letter_name_if_final_boss = "Domino's snakes."

    _gender = ("they", "them", "their", "theirs", "themselves")
    _marrymore_name = "Domino"
    _marrymore_single_gender = ("he", "him", "his", "his", "himself")

    _npc_models = [DominoLargeObject, DominoSmallObject]
    _statue_npc = DominoStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """DOMINO: I’m busy wallowing in\n misery at my defeat here.[await][pause] Get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Uh oh, you cracked the code...\n I don’t like where this is going...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Cloaker and Domino’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n CLOAKER and DOMINO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """DOMINO: Guess you’re tougher\n than I thought...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n DOMINO: So, you’ve returned...![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """DOMINO: I don’t like where this is\n going...[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I always enjoy a nice Bubble Tea[await]\n ...after CLOBBERING TIME!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ I always enjoy a nice Bubble Tea[await]\n ...after CLOBBERING TIME!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`![await][page]\n We TOLD you to put your dukes up with `SEASIDE_BOSS`![await]\n You’d better be ready! We saw `VOLCANO_BOSS_DESCRIPTION` near the volcano![await]\n We think those snakes belong to `FINAL_BOSS_NAME` They sound like WEAKLINGS![await]\n It would be shameful if they defeated you.[await]\n Stop by the ship if you want to play! Or see a blockable Carni-Kiss![await][page]\n\n              IT’S CLOBBERING TIME!!\n                       Cloaker & Domino[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big brick! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Domino must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """DOMINO: Hee hee hee... You still\n need to find [0x7024] more item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """DOMINO: Hee hee hee... You found\n all the gear, but you missed the\n stuff lying around this room![await]\n I don’t like where this is going...[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Cloaker and Domino are busy right\n now, so they can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Cloaker and Domino.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """DOMINO: Hee hee hee... So you’ve\n found our little town! Boring,\n isn’t it?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Domino...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """DOMINO: Hee hee hee... So you’re\n challenging the dojo master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hee hee hee... Wanna fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hee hee hee... Wanna fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the people\n next door.[await][page]\n They’re always mumbling about\n Weaklings-this and Snake-that.[await][page]\n Sometimes I’d like to ask them what\n they’re babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn’t been\n getting me the results I wanted.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn’t been\n getting me the results I wanted.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Cloaker and Domino are busy right\n now, so they can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Cloaker and Domino.[await]""",
    }


__all__ = ["CloakerDominoBossFight"]
