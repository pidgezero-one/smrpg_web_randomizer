from __future__ import annotations
from randomizer.data.enemies.enemies import (FORMLESSEnemy, MOKURAEnemy)
from randomizer.data.packs.pack_collection import (FORM0314_ONE_FORMLESS_ONE_MOKURA)
from randomizer.data.physical_objects.bosses import (MokuraLargeObject, MokuraSmallObject, MokuraStatueObject)
from randomizer.data.physical_objects.henchmen import (MokuraHenchman)
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
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class MokuraBossFight(BossFightPrize):
    _text = "Mokura"
    _formation = FORM0314_ONE_FORMLESS_ONE_MOKURA
    _members = [
        FormationMember(FORMLESSEnemy, 167, 135),
        FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a noxious cloud floating"
    _seaside_letter_name_if_final_boss = "Mokura's collective."
    _seaside_letter_name_if_final_boss_remake = "Gassox' collective."
    _remake_name = "Gassox"
    _anchor_enemy = MOKURAEnemy
    _hp_slice_excluded_enemies = [FORMLESSEnemy]

    _npc_models = [MokuraLargeObject, MokuraSmallObject]
    _statue_npc = MokuraStatueObject

    _tiny_henchmen = [
        BossFightHenchman(monster=MOKURAEnemy, model=MokuraHenchman),
    ]

    _gender = ("it", "it", "its", "its", "itself")

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """[center]\nMOKURA: Uhh... Go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """[center]\nDuh, huh, huh...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Mokura’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped MOKURA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nMOKURA: Hmm...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MOKURA: What’re you doing in my\n secret lair?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MOKURA: I oughta go back to\n being invisible...[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Mmm...uhhh. Cotton Candy![await]\n ...It’s...so...airy...YUM![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Mmm...uhhh. Cotton Candy![await]\n ...It’s...so...airy...YUM![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n (...Is this invisible ink?)[await][page]\n“Defeated `SEASIDE_BOSS`. Good.”[await]\n“Sensed... `VOLCANO_BOSS_DESCRIPTION` near volcano...”[await]\n“Ethereal bond with `FINAL_BOSS_NAME`”[await][page]\n(This last part just reeks of\n flatulence...) [await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big cloud! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Mokura must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MOKURA: Uhh... You need [0x7024] more\n item(s)...[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """MOKURA: Duhh... Go get the rest\n of the stuff in this room.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Mokura’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Mokura.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nMOKURA: Mwa, ha, ha![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Mokura...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MOKURA: Uhh... Are you... gonna\n beat the Dojo Master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Uhh... Hi there.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Uhh... Hi there.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Secret-this and Gas-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """[center]\nMOKURA: Clouds can’t jump...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """[center]\nMOKURA: Clouds can’t jump...[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """[center]\nGASSOX: Uhh... Go away![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Gassox’ place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped GASSOX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nGASSOX: Hmm...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """GASSOX: What’re you doing in my\n secret lair?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """GASSOX: I oughta go back to\n being invisible...[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Gassox must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """GASSOX: Uhh... You need [0x7024] more\n item(s)...[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """GASSOX: Duhh... Go get the rest\n of the stuff in this room.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Gassox is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Gassox.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nGASSOX: Mwa, ha, ha![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Gassox...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """GASSOX: Uhh... Are you... gonna\n beat the Dojo Master?[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """[center]\nGASSOX: Clouds can’t jump...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """[center]\nGASSOX: Clouds can’t jump...[await]""",
    }


__all__ = ["MokuraBossFight"]
