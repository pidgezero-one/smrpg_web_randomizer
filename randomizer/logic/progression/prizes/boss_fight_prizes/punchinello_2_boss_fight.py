from __future__ import annotations
from randomizer.data.enemies.enemies import (PUNCHINELLO2Enemy, STRONGBOBOMB1Enemy, STRONGBOBOMB2Enemy, STRONGBOBOMB3Enemy, STRONGBOBOMB4Enemy)
from randomizer.data.packs.pack_collection import (FORM0124_ONE_PUNCHINELLO2_ONE_STRONGBOBOMB3_ONE_STRONGBOBOMB1_ONE_STRONGBOBOMB4_ONE_STRONGBOBOMB2)
from randomizer.data.physical_objects.bosses import (Punchinello2LargeObject, Punchinello2SmallObject, PunchinelloStatueObject)
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


class Punchinello2BossFight(BossFightPrize):
    _text = "Punchinello 2"
    _formation = FORM0124_ONE_PUNCHINELLO2_ONE_STRONGBOBOMB3_ONE_STRONGBOBOMB1_ONE_STRONGBOBOMB4_ONE_STRONGBOBOMB2
    _members = [
        FormationMember(PUNCHINELLO2Enemy, 188, 116),
        FormationMember(STRONGBOBOMB3Enemy, 145, 103, hidden_at_start=True),
        FormationMember(STRONGBOBOMB1Enemy, 150, 129, hidden_at_start=True),
        FormationMember(STRONGBOBOMB4Enemy, 182, 142, hidden_at_start=True),
        FormationMember(STRONGBOBOMB2Enemy, 223, 142, hidden_at_start=True),
    ]
    _anchor_enemy = PUNCHINELLO2Enemy
    _hp_slice_excluded_enemies = [
        STRONGBOBOMB3Enemy,
        STRONGBOBOMB1Enemy,
        STRONGBOBOMB4Enemy,
        STRONGBOBOMB2Enemy,
    ]

    _name = "Punchinello"
    _seaside_letter_name_if_seaside_boss = "Hothead"
    _seaside_letter_name_if_volcano_boss = "a demolitionist stomping"
    _seaside_letter_name_if_final_boss = "Punchinello's demo team."

    _npc_models = [Punchinello2LargeObject, Punchinello2SmallObject]
    _statue_npc = PunchinelloStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PUNCHINELLO: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So... You figured out my\n password.[await]\n If you’re not here for an\n autograph, I’ll have to test you\n once more to let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Punchinello’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n PUNCHINELLO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PUNCHINELLO: Grrr... I’ll never get famous at this rate![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PUNCHINELLO: You’ve come back to\n visit? I truly must be famous![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PUNCHINELLO: They say I’m a hot\n head, so it’s a bad idea to stand\n on my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ WATCH ME DRINK THIS TOBASCO![await]\n I’m gonna be youtube-famous![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ WATCH ME DRINK THIS TOBASCO![await]\n I’m gonna be youtube-famous![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n WHAT’S UP CHAT?![await][page]\n I just watched a HYPE fight versus `SEASIDE_BOSS`.  Oh.  Em.  Gee.[await]\n My Bob-omb army told me about `VOLCANO_BOSS_DESCRIPTION` near the volcano. Fuse is LIT!![await]\n I smell a collab video with `FINAL_BOSS_NAME`[await]\n Don’t forget to tune in for my 100 follower special, where I’ll play Bob-omb roulette with watermelons![await][page]\n\n           Like, Share, and Subscribe!\n                              Punchinello[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like celebrity! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Punchinello must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PUNCHINELLO: Huh?[delay_30] What the hay?[await]\n Where are the other [0x7024] item(s)?[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """PUNCHINELLO: Huh?[delay_30] You’ve got all the stuff we need\n for the ceremony?[await]\n Great.[delay] But aren’t there a few more\n things to grab in this room?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Punchinello’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Punchinello.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PUNCHINELLO: Hmmm... [delay]Huh?\n [delay]A visitor? [delay]Well, there’s not much\n to do around here.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Punchinello...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PUNCHINELLO: A challenge from\n the dojo master, eh? Let’s see\n where this goes.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I’m here to fight)\n  [select] (Sorry, wrong number)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I’m here to fight)\n  [select] (Sorry, wrong number)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Bomb-this and Famous-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Punchinello’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Punchinello.[await]""",
    }


__all__ = ["Punchinello2BossFight"]
