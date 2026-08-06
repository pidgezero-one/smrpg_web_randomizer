from __future__ import annotations
from randomizer.data.enemies.enemies import (CROCO1Enemy)
from randomizer.data.packs.pack_collection import (FORM0273_ONE_CROCO1)
from randomizer.data.physical_objects.bosses import (Croco1Object, CrocoStatueObject)
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


class Croco1BossFight(BossFightPrize):
    _text = "Croco 1"
    _formation = FORM0273_ONE_CROCO1
    _members = [
        FormationMember(CROCO1Enemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a thieving reptile dashing"
    _seaside_letter_name_if_final_boss = "Croco's flunkies."
    _name = "Croco"

    _npc_models = [Croco1Object]
    _statue_npc = CrocoStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n CROCO: Get the heck outta here![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Alright, alright, so ya figured out\n my password! But I ain’t goin’\n down without a fight![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CROCO: Enough already, get outta\n here![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CROCO: Back already? How ’bout a\n drink?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n    CROCO: ’Dis some kinda joke?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Wanna know how I run so fast?[await]\n Chug some Honey Syrup, chump![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Wanna know how I run so fast?[await]\n Chug some Honey Syrup, chump![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n ’Sup Half-Wits?![await][page]\n Did it take you 500 years to beat `SEASIDE_BOSS`?[await]\nWhile chasing my next heist, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano. Seems... nice.[await]\nI better get a crew together with `FINAL_BOSS_NAME`[await]\nI’m telling you this because I want this to be a challenge this time.[await]\nI bet this bazooka that I lifted from that toad “guard” will be useful![await][page]\n\n                                    Seeya!\n                                     Croco[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Croco must have gotten\n lost on his way here.""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big reptile! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CROCO: What’s this?[await][pause] You fools’re\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """CROCO: What’s this? You found all of `MARRYMORE_CHARACTER`’s things?[await]\n You’re missing a few things in this room, though. Don’t take another 50 years to find them.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CROCO: Whaddya doin’ hangin\n ’round here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Croco...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CROCO: Think ya can beat the dojo\n master, chump? I’d like to see ya\n try![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Croco’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped CROCO!![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Croco’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Croco.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Croco’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Croco.[await]""",
    }


__all__ = ["Croco1BossFight"]
