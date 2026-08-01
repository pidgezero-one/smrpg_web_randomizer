from __future__ import annotations
from randomizer.data.enemies.enemies import (JAGGEREnemy)
from randomizer.data.packs.pack_collection import (FORM0299_ONE_JAGGER)
from randomizer.data.physical_objects.bosses import (TerrapinObject, TerrapinStatueObject)
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
    DI3057_MONSTRO_SUPERBOSS_PROMPT,
    DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT,
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)


class JaggerBossFight(BossFightPrize):
    _text = "Jagger"
    _formation = FORM0299_ONE_JAGGER
    _members = [
        FormationMember(JAGGEREnemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a turtle shoulder-charging"
    _seaside_letter_name_if_final_boss = "Jagger's compatriots."

    _npc_models = [TerrapinObject]
    _statue_npc = TerrapinStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JAGGER: It’d be fun to fight\n again, but I need a nap.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Wow, you figured out the\n password! Come on in and let’s\n have a spar![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Jagger’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped JAGGER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """JAGGER: Wow, what a fight! I\n better think about what I’m gonna\n do to win next time...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JAGGER: Welcome back! I’ve been\n training hard for our next fight,\n whenever that may be![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JAGGER: `MAIN_CHARACTER_NAME`, I can’t\n jump as high as you. Is this\n really necessary?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ My Sensei’s drink is gross...[await]\n Here, my Black Tea is WAY better.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ My Sensei’s drink is gross...[await]\n Here, my Black Tea is WAY better.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hi `MAIN_CHARACTER_NAME`![await][page]\n I saw you give the business to `SEASIDE_BOSS`! It was a shell of a good hit!! [await]\n While out training, I saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I hear they run with `FINAL_BOSS_NAME`[await]\n I hope you’ve been practicing your timed blocks! I’ll know the next time I use Terrapunch on you![await][page]\n\n                          You can do it!\n                                    Jagger[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big turtle! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jagger must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JAGGER: Oh, wow, you’ve already\n found [0x7000] item(s)![await][pause] I bet you’ll find\n the last [0x7024] in no time.[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """JAGGER: Hey, thanks for getting\n all of this gear! Why don’t you go\n grab the last few things in here?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jagger’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jagger.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """JAGGER:\n[center]Hi, `MAIN_CHARACTER_NAME`![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jagger...\n in his house. He is...the most\n respected person here.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. May I help you?[await]\n  [select] (Let’s fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello. May I help you?[await]\n  [select] (Let’s fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Dojo-this and Sensei-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JAGGER: Sensei, the new regimen\n will strengthen us, right?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Jagger’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Jagger.[await]""",
    }


__all__ = ["JaggerBossFight"]
