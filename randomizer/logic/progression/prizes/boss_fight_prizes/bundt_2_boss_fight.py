from __future__ import annotations
from randomizer.data.enemies.enemies import (BUNDT2Enemy, CANDLEEnemy, RASPBERRY2Enemy, TORTE2Enemy)
from randomizer.data.packs.pack_collection import (FORM0137_ONE_BUNDT2_ONE_RASPBERRY2_TWO_TORTE2_ONE_CANDLE)
from randomizer.data.physical_objects.bosses import (Bundt2LargeObject, Bundt2SmallObject, BundtStatueObject)
from randomizer.data.variables.battle_event_names import (BE0017_BEGIN_BUNDT_POSTGAME)
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
    DI2062_APPRENTICE_CHEF,
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


class Bundt2BossFight(BossFightPrize):
    _text = "Bundt 2"
    _formation = FORM0137_ONE_BUNDT2_ONE_RASPBERRY2_TWO_TORTE2_ONE_CANDLE
    _members = [
        FormationMember(BUNDT2Enemy, 199, 127),
        FormationMember(RASPBERRY2Enemy, 199, 119),
        FormationMember(TORTE2Enemy, 199, 151),
        FormationMember(TORTE2Enemy, 135, 119),
        FormationMember(CANDLEEnemy, 0, 0),
    ]
    _anchor_enemy = BUNDT2Enemy
    _force_start_event = BE0017_BEGIN_BUNDT_POSTGAME

    _seaside_letter_name_if_seaside_boss = "the Cake"
    _seaside_letter_name_if_volcano_boss = "a possessed cake walking"
    _seaside_letter_name_if_final_boss = "Bundt's dinner guests."
    _name = "Bundt"

    _gender = ("it", "it", "its", "its", "itself")

    _npc_models = [Bundt2LargeObject, Bundt2SmallObject]
    _statue_npc = BundtStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n[center]BUNDT: La la la la la la la la la~[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ What a surprise! [delay_30]Welcome![await]\n Let me warm up for the feast![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Bundt’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped BUNDT!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BUNDT: Oh...! My beautiful body![await][pause]\n Please go away while I recover![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BUNDT: Come back to celebrate a\n wedding? At least try and eat me\n this time...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BUNDT: OH! MY CANDLES![await]""",
        DI1782_SHIP_BOSS_DRINK: """ I’ve got my own frosting, thanks.[await]\n “Happy” Frogs taste best, though![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ I’ve got my own frosting, thanks.[await]\n “Happy” Frogs taste best, though![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings and Salutations![await][page]\n I can’t get over how quickly you dispatched `SEASIDE_BOSS`![await]\n My dinner guests informed me of `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I heard they’re having a reunion with `FINAL_BOSS_NAME`[await]\n I’ve gotten hungry aboard this ship. You wouldn’t believe how much you can miss your chefs and creams. [await]\n Come visit and have a slice![await][page]\n\n       Frosting my way to victory,\n                                     Bundt[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: This masterpiece is\n our latest creation... wait...[await]""",
        DI2062_APPRENTICE_CHEF: """APPRENTICE: Chef Torte! [delay]Why\n did we make another Bundt?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bundt must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BUNDT: Hmm?[delay] You look like you\n could use a break![await][pause] Come back with\n the other [0x7024] item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """BUNDT: You found all the wedding\n gear, but you’re missing a few\n things in this room.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Bundt is busy right now, so it\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Bundt.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BUNDT: Greetings and salutations!\n Welcome to our quiet little town![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Bundt...\n in his house. He is...the most\n respected dessert here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BUNDT: What a fierce battle![await][pause] That\n was nothing compared to the dojo\n master, you know.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What’s this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What’s this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Candle-this and Frosting-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Bundt is busy right now, so it\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Bundt.[await]""",
    }


__all__ = ["Bundt2BossFight"]
