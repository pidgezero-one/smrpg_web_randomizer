from __future__ import annotations
from randomizer.data.enemies.enemies import (BAHAMUTTEnemy2, CHESTEREnemy)
from randomizer.data.packs.pack_collection import (FORM0269_ONE_CHESTER_ONE_BAHAMUTTENEMY2)
from randomizer.data.physical_objects.bosses import (ChesterLargeObject, ChesterSmallObject, MimicStatueObject)
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


class ChesterBossFight(BossFightPrize):
    _text = "Chester"
    _formation = FORM0269_ONE_CHESTER_ONE_BAHAMUTTENEMY2
    _members = [
        FormationMember(CHESTEREnemy, 183, 127),
        FormationMember(BAHAMUTTEnemy2, 135, 119, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a purple box sliding about"
    _seaside_letter_name_if_final_boss = "Chester's monsters."
    _seaside_letter_name_if_final_boss_remake = "Comeon's monsters."
    _remake_name = "Comeon"

    _npc_models = [ChesterLargeObject, ChesterSmallObject]
    _statue_npc = MimicStatueObject

    _anchor_enemy = CHESTEREnemy
    _hp_slice_excluded_enemies = [BAHAMUTTEnemy2]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CHESTER: Go on, take it. Just let\n me go back to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Quit draggin’ your feet! Get in\n here and let’s fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Chester’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n CHESTER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nCHESTER: (How embarrassing...)[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CHESTER: You know, I’m kind of a\n big deal over in Bowser’s Keep.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CHESTER: This is unnecessary. Get\n off me![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Leave me alone with my precious[await]\n ’92 Napper Cabernet Sauivignon.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Leave me alone with my precious[await]\n ’92 Napper Cabernet Sauivignon.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`:[await][page]\n I’m too old for this nonsense with `SEASIDE_BOSS`, good luck.[await]\n Just to see if I could, I summoned `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n It seems they’re associated with`FINAL_BOSS_NAME`[await]\n I’ve been belching up monsters for a LONG time, and I’ve never seen anything this rude.[await]\n Fix it, and I MIGHT forget you opened my box.[await][page]\n\n    Go do something useful for once.\n                                   Chester[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Chester must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CHESTER: Don’t bother me unless\n you have found [0x7024] more item(s).[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """CHESTER: Don’t try to proceed\n until you’ve found everything in\n this room.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Chester’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Chester.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CHESTER:\n[center]This town is pretty quiet.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Chester...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """[center]\nCHESTER: Now THIS I gotta see.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You’re interrupting my sleep.[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You’re interrupting my sleep.[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Treasure-this and Dragon-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """[center]\nCHESTER: I don’t even have legs![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """[center]\nCHESTER: I don’t even have legs![await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """COMEON: Go on, take it. Just let\n me go back to sleep.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Comeon’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n COMEON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nCOMEON: (How embarrassing...)[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """COMEON: You know, I’m kind of a\n big deal over in Bowser’s Keep.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`:[await][page]\n I’m too old for this nonsense with `SEASIDE_BOSS`, good luck.[await]\n Just to see if I could, I summoned `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n It seems they’re associated with`FINAL_BOSS_NAME`[await]\n I’ve been belching up monsters for a LONG time, and I’ve never seen anything this rude.[await]\n Fix it, and I MIGHT forget you opened my box.[await][page]\n\n    Go do something useful for once.\n                                    Comeon[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Comeon must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """COMEON: Don’t bother me unless\n you have found [0x7024] more item(s).[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """COMEON: Don’t try to proceed\n until you’ve found everything in\n this room.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Comeon’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Comeon.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """COMEON:\n[center]This town is pretty quiet.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Comeon...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """[center]\nCOMEON: Now THIS I gotta see.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """[center]\nCOMEON: I don’t even have legs![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """[center]\nCOMEON: I don’t even have legs![await]""",
    }


__all__ = ["ChesterBossFight"]
