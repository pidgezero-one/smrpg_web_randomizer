from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (HAMMERBROEnemy)
from randomizer.data.packs.pack_collection import (FORM0293_TWO_HAMMERBRO)
from randomizer.data.physical_objects.bosses import (HammerBroLargeObject, HammerBroSmallObject, HammerBroStatueObject)
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
from randomizer.data.variables.variable_names import (MAP_BANDITS_WAY, MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (SetBit)
from randomizer.types.flags import (BanditsWayGate, BanditsWayGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class HammerBrosFight(BossFightPrize):
    _text = "Hammer Bros"
    _name = "Hammer Bro"
    _formation = FORM0293_TWO_HAMMERBRO
    _members = [
        FormationMember(HAMMERBROEnemy, 135, 127),
        FormationMember(HAMMERBROEnemy, 199, 143),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            BanditsWayGate, BanditsWayGating.HAMMER_BRO
        ):
            output.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        return EventScript(output)

    _npc_models = [HammerBroLargeObject, HammerBroSmallObject]
    _statue_npc = HammerBroStatueObject

    _seaside_letter_name_if_sunken_ship_boss = "the Hammer Bros"
    _seaside_letter_name_if_volcano_boss = "two brothers dancing around"
    _seaside_letter_name_if_final_boss = "the Hammer Bros' pals."

    _gender = ("they", "them", "their", "theirs", "themselves")
    _marrymore_name = "Hammer Bro"
    _marrymore_single_gender = ("he", "him", "his", "his", "himself")

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HAMMER BRO: Alright already, you won, now go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you figured it out... But you gotta get past my hammer to get through![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HAMMER BRO: ...grumble...[delay] My hammer’s embarrassed about losing...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HAMMER BRO:\n[center]What’re YOU lookin’ at?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HAMMER BRO: Look buddy, you already won, you can stop\n taunting my hammer now.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ After getting hammered, [await]\n I always drink Carrot Juice.[await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ After getting hammered, [await]\n I always drink Carrot Juice.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`![await][page]\n My bro and I saw you squash `SEASIDE_BOSS`! Nice one![await]\n My bro and his hammer say they saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n We’ve nailed them down as one of `FINAL_BOSS_NAME`[await]\n Listen, my bro is on me about loanin’ you my hammer.[await]\n Whaddaya say you bring me back an upgrade to pummel him with? Do me a solid![await][page]\n\n                                  Thanks!\n                         Hammer Bro #2[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It’ll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big hammer! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bro must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HAMMER BRO: You better find [0x7024]\n more of `MARRYMORE_CHARACTER`’s things,\n or my hammer’ll be angry![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """HAMMER BRO: You found all of `MARRYMORE_CHARACTER`’s things?[await]\n Good job, bozo, but you’re still missing a few things in this room![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """HAMMER BRO:\n[center]What’re YOU lookin’ at?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find the Hammer Bro...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HAMMER BRO: The dojo master\n takes on 3 different forms.\n Me, though? I’m just a hammer.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ This’d BETTER be important![await]\n  [select] (Nice hammer. Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ This’d BETTER be important![await]\n  [select] (Nice hammer. Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Hammer-this and Hammer-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HAMMER BRO: I guess you were\n tougher than I thought![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HAMMER BRO: I guess you were\n tougher than I thought![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to the Hammer Bros’ place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n the HAMMER BROS!![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Hammer Bros are busy right\n now, so they can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Hammer Bros.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Hammer Bros are busy right\n now, so they can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Hammer Bros.[await]""",
    }


__all__ = ["HammerBrosFight"]
