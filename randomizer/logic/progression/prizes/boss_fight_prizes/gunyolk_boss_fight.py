from __future__ import annotations
from randomizer.data.enemies.enemies import (FACTORYCHIEFEnemy, GUNYOLKEnemy)
from randomizer.data.packs.pack_collection import (FORM0261_ONE_GUNYOLK_ONE_FACTORYCHIEF)
from randomizer.data.physical_objects.bosses import (FactoryChiefObject, FactoryChiefStatueObject)
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


class GunyolkBossFight(BossFightPrize):
    _text = "Gunyolk"
    _formation = FORM0261_ONE_GUNYOLK_ONE_FACTORYCHIEF
    _members = [
        FormationMember(GUNYOLKEnemy, 199, 103),
        FormationMember(FACTORYCHIEFEnemy, 231, 151),
    ]
    _seaside_letter_name_if_seaside_boss = "the Chief"
    _seaside_letter_name_if_volcano_boss = "a big machine rolling"
    _seaside_letter_name_if_final_boss = "the Factory Chief's goons."
    _gender = ("it", "it", "its", "its", "itself")

    _npc_models = [FactoryChiefObject]
    _statue_npc = FactoryChiefStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """FACTORY CHIEF: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you solved it?[delay_30]\n Too bad, this is the end of the line\n for you! I won’t let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to the Gunyolk’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n the GUNYOLK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """FACTORY CHIEF: Harrumph! Get out\n of here before I invent something\n even stronger![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """FACTORY CHIEF: I’m surprised to\n see you back here! I don’t have any\n new inventions to show yet.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """FACTORY CHIEF: Harrumph! I should\n invent myself a spiky hat![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Who do I have to Breaker Beam[await]\n to get a cuppa Coffee ’round here?[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Who do I have to Breaker Beam[await]\n to get a cuppa Coffee ’round here?[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n              Memorandum[await][page]\n `MAIN_CHARACTER_NAME` dispatched to handle `SEASIDE_BOSS`.[await]\n Real estate acquisition stalled by `VOLCANO_BOSS_DESCRIPTION` near volcano.[await]\n Competition associated with `FINAL_BOSS_NAME`[await]\n Report all conversations involving the words “union”, “living wage”, or “benefits” immediately.[await][page]\n\n                      Do more with less.\n                                -The Chief[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big ninja! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Chief must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """FACTORY CHIEF: Harrumph! You’re\n still missing [0x7024] more item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """FACTORY CHIEF: Harrumph! You\n found all the gear, but there are\n still items in this room![await]\n What kind\n of worker misses those?![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Gunyolk is busy right now, so\n it can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Gunyolk.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """FACTORY CHIEF: Harrumph! What’re\n you doing here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find the Factory Chief...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """FACTORY CHIEF: Harrumph! Just\n because you beat me, doesn’t mean\n you can beat the dojo master![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Did you come here to fight me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Did you come here to fight me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Ninja-this and Invention-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """FACTORY CHIEF: I’ll out-jump you\n if it’s the last thing I do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """FACTORY CHIEF: I’ll out-jump you\n if it’s the last thing I do![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Gunyolk is busy right now, so\n it can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Gunyolk.[await]""",
    }


__all__ = ["GunyolkBossFight"]
