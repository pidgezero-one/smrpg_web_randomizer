from __future__ import annotations
from randomizer.data.enemies.enemies import (JINX1Enemy)
from randomizer.data.packs.pack_collection import (FORM0288_ONE_JINX1)
from randomizer.data.physical_objects.bosses import (Jinx1SmallObject, JinxStatueObject)
from randomizer.data.variables.battle_event_names import (BE0071_JINX_USES_TRIPLE_KICK)
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
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class Jinx1BossFight(BossFightPrize):
    _text = "Jinx 1"
    _formation = FORM0288_ONE_JINX1
    _members = [
        FormationMember(JINX1Enemy, 183, 127),
    ]
    _force_start_event = BE0071_JINX_USES_TRIPLE_KICK
    _seaside_letter_name_if_volcano_boss = "a small figure blinking"
    _seaside_letter_name_if_final_boss = "Jinx's kouhai."
    _name = "Jinx"

    _npc_models = [Jinx1SmallObject]
    _statue_npc = JinxStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you’ve figured out the\n password. But, I’m not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Jinx’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nJINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ We’re warming up `MAIN_CHARACTER_NAME`![await]\n But first, a Green Tea break![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ We’re warming up `MAIN_CHARACTER_NAME`![await]\n But first, a Green Tea break![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,[await][page]\n Have you mastered your training with `SEASIDE_BOSS`?[await]\n I sense your next challenge is `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They battle in the old style of `FINAL_BOSS_NAME`[await]\n Complete this task, and you will be prepared for our rematch.[await]\n Fail, and you need not ever show your face on my ship again.[await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jinx must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don’t let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """JINX: You may have found all the\n gear, but there is more for you to\n find in this room. Get to work![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """[center]\nJINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Jinx is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Jinx.[await]""",
    }


__all__ = ["Jinx1BossFight"]
