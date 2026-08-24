from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (GRATEGUYEnemy, KNIFEGUYEnemy)
from randomizer.data.packs.pack_collection import (FORM0287_ONE_KNIFEGUY_ONE_GRATEGUY)
from randomizer.data.physical_objects.bosses import (GrateGuyLargeObject, GrateGuySmallObject, GrateGuyStatueObject)
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
    DI1786_LETTER_FROM_SHIP_BOSS,
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
from randomizer.data.variables.variable_names import (BOOSTER_HILL_CLOSED, MARRYMORE_BACKDOOR_OPEN)
from randomizer.types.prize import (BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (ClearBit, SetBit)
from randomizer.types.flags import (BoosterHillGate, BoosterHillGating, MarrymoreGate, MarrymoreGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)


class KnifeGuyGrateGuyBossFight(BossFightPrize):
    _text = "Knife Guy & Grate Guy"
    _formation = FORM0287_ONE_KNIFEGUY_ONE_GRATEGUY
    _members = [
        FormationMember(KNIFEGUYEnemy, 151, 119),
        FormationMember(GRATEGUYEnemy, 199, 143),
    ]
    _seaside_letter_name_if_seaside_boss = "the Clowns"
    _seaside_letter_name_if_volcano_boss = "a couple clowns bouncing"
    _seaside_letter_name_if_final_boss = "Grate Guy's clowns."

    _npc_models = [GrateGuyLargeObject, GrateGuySmallObject]
    _statue_npc = GrateGuyStatueObject

    _gender = ("they", "them", "their", "theirs", "themselves")
    _marrymore_name = "Grate Guy"
    _marrymore_single_gender = ("he", "him", "his", "his", "himself")

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """GRATE GUY: Get lost, buddy, I’m\n busy![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, a patron![delay_30] Come on in and let’s\n get this show on the road![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Knife Guy and Grate Guy’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped KNIFE GUY\n and GRATE GUY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """GRATE GUY: Yikes, you’re pretty\n tough! I need some time to recover.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """GRATE GUY: It’s so boring\n around here... Hey, wanna play\n “Look the other way” with me?[await][page]\n Hah! [delay_30]Just kidding![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """GRATE GUY: Sorry, `MAIN_CHARACTER_NAME`, but jumping on my head isn’t going to teach you Blizzard.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Of course I didn’t shake it up!![await]\n Go on, have a Root Beer!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ Of course I didn’t shake it up!![await]\n Go on, have a Root Beer!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """KNIFE GUY: No, I’m not giving you the Bright Card down here![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Heya `MAIN_CHARACTER_NAME`,[await][page]\n Looks like you totally thrashed `SEASIDE_BOSS`. Whoopdy do![await]\n Knife Guy tells me he saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They’re in a traveling circus with `FINAL_BOSS_NAME`[await]\n I was going to open another casino, but Knife Guy dropped the ball on the building permits.[await]\n So now our ship is sunk. Stop by sometime, we’re always down to clown.[await][page]\n\n                                    Later!\n                 Grate Guy & Knife Guy[await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big clown! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Grate Guy must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """GRATE GUY: Hm?[await][pause] Well, you took all\n the trouble to find [0x7000] item(s),\n so... keep looking for the other [0x7024]![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """GRATE GUY: Hm?[await][pause] You took all the trouble to find all\n the wedding gear, but not pick up\n the gear lying around this room?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Knife Guy and Grate Guy are busy\n right now, so they can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Knife Guy and\n Grate Guy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """GRATE GUY: Gee, it sure is boring\n around here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Grate Guy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """GRATE GUY: The dojo master’s\n much tougher than I am. Think you\n can win?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Welcome! What brings you here?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Welcome! What brings you here?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the people\n next door.[await][page]\n They’re always mumbling about\n Knife-this and Casino-that.[await][page]\n Sometimes I’d like to ask them what\n they’re babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """GRATE GUY: Look, `MAIN_CHARACTER_NAME`! I’ve been training so hard, that my ball jumps with me![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """GRATE GUY: Look, `MAIN_CHARACTER_NAME`! I’ve been training so hard, that my ball jumps with me![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Knife Guy and Grate Guy are busy\n right now, so they can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Knife Guy and\n Grate Guy.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            BoosterHillGate, BoosterHillGating.KGGG
        ):
            output.extend([ClearBit(BOOSTER_HILL_CLOSED)])
        if world.settings.is_flag_value(
            MarrymoreGate, MarrymoreGating.KGGG
        ):
            output.extend([SetBit(MARRYMORE_BACKDOOR_OPEN)])
        return EventScript(output)


__all__ = ["KnifeGuyGrateGuyBossFight"]
