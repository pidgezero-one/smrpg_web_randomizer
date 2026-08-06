from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (BODYGUARDEnemy, MACKEnemy)
from randomizer.data.packs.pack_collection import (FORM0289_ONE_MACK_FOUR_BODYGUARD)
from randomizer.data.physical_objects.bosses import (MackLargeObject, MackMediumObject, MackSmallObject, MackStatueObject)
from randomizer.data.physical_objects.henchmen import (ShysterHenchman)
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
    DI2832_OCCUPIED_SEASIDE_INNKEEPER,
    DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING,
    DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED,
    DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
    DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED,
    DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
    DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER,
    DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
    DI3057_MONSTRO_SUPERBOSS_PROMPT,
    DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT,
    DI3072_TOWER_HENCHMAN_3_WINDOW,
    DI3073_TOWER_HENCHMAN_3,
    DI3338_MONSTRO_SUPERBOSS_HINT,
    DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    DI3353_DOJO_BOSS_2_FULLY_DEFEATED,
    DI4060_NEED_TO_DO_CHAPEL_CHECKS,
)
from randomizer.data.variables.room_names import (R333_KERO_SEWERS_ENTRANCE)
from randomizer.data.variables.variable_names import (SEWERS_CLOSED)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import (NPC_1)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (ClearBit, RemoveObjectFromSpecificLevel)
from randomizer.types.flags import (KeroSewersGate, KeroSewersGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MackBossFight(BossFightPrize):
    _text = "Mack"
    _formation = FORM0289_ONE_MACK_FOUR_BODYGUARD
    _members = [
        FormationMember(MACKEnemy, 199, 119),
        FormationMember(BODYGUARDEnemy, 135, 111),
        FormationMember(BODYGUARDEnemy, 151, 127),
        FormationMember(BODYGUARDEnemy, 183, 143),
        FormationMember(BODYGUARDEnemy, 215, 151),
    ]
    _anchor_enemy = MACKEnemy

    _seaside_letter_name_if_volcano_boss = "a small sword jumping"
    _seaside_letter_name_if_final_boss = "Mack's shysters."
    _seaside_letter_name_if_final_boss_remake = "Claymorton's guys."

    _remake_name = "Claymorton"

    _npc_models = [MackLargeObject, MackMediumObject, MackSmallObject]
    _statue_npc = MackStatueObject

    _mook_henchmen = [BossFightHenchman(monster=BODYGUARDEnemy, model=ShysterHenchman)]
    _character_henchmen = [
        BossFightHenchman(monster=BODYGUARDEnemy, model=ShysterHenchman),
        BossFightHenchman(monster=BODYGUARDEnemy, model=ShysterHenchman),
        BossFightHenchman(monster=BODYGUARDEnemy, model=ShysterHenchman),
        BossFightHenchman(monster=BODYGUARDEnemy, model=ShysterHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MACK: Party’s over. I’m going to\n sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Listen, bub![await]\n You may have figured out my\n password, but you still gotta get\n past me if you want through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Mack’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped MACK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """[center]\nMACK: Guess the party’s over.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MACK: Hey `MAIN_CHARACTER_NAME`! Come back to crash our party?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MACK: OK, I get it, you can bounce\n too.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I don’t care what kinda party it is![await]\n I drink Milk so I can be like Exor!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ I don’t care what kinda party it is![await]\n I drink Milk so I can be like Exor!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """BODYGUARD: There’s no hard\n feelings. We’re all just trying to\n have a good time.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Yo `MAIN_CHARACTER_NAME`![await][page]\n I heard you left and threw down with `SEASIDE_BOSS`![await]\n The Shysters on lookout saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They got the good stuff from `FINAL_BOSS_NAME`[await]\n We’d better get back aboard before any other Shyster party fouls. I heard Exor might even show up![await][page]\n\n                             Hang loose!\n                                     Mack[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """BODYGUARD: Hop on the trampoline\n in the next room. It’ll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """BODYGUARD: There’s no hard\n feelings. We’re all just trying to\n have a good time.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """BODYGUARD: There’s no hard\n feelings. We’re all just trying to\n have a good time.[await]""",
        DI2061_HEAD_CHEF: """BODYGUARD: Doesn’t this cake\n look just like Mack?[await]""",
        DI2062_APPRENTICE_CHEF: """BODYGUARD: We’ve gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Mack must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MACK: I’m not happy to delay the\n party, but we can’t get started\n until you find [0x7024] more item(s)![await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """MACK: Great, you found all of `MARRYMORE_CHARACTER`’s stuff.[await]\n But we can’t start the party until you clean up all the junk in this room, too.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Mack’s busy right now, so he can’t\n play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Mack.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n[center]MACK: What’re YOU doing here?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Yo! You look tired.[delay] How ’bout a\n night on the house?[await]\n  [select] (Thanks)\n  [select] (I’ll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can’t get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Mack’s house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Yo! It’s fine if you hang out in\n town, but... [delay]stay away from the\n shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There’s something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there’s a wall of boxes\n hiding a treasure chest. It’s pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We’ll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ You trying to snoop on what I’m\n buying here?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n[center]What’re YOU lookin’ at?[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n[center]Beat it, bub![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MACK: Think you’re gonna beat the\n dojo master today?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You come to crash my party?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You come to crash my party?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Bouncing-this and Party-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MACK: I guess you CAN bounce\n after all.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MACK: I guess you CAN bounce\n after all.[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CLAYMORTON: Party’s over. I’m\n going to sleep.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Claymorton’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n CLAYMORTON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CLAYMORTON:\n[center]Guess the party’s over.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CLAYMORTON: Hey `MAIN_CHARACTER_NAME`! Come back to crash our party?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CLAYMORTON: OK, I get it, you can\n bounce too.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Yo `MAIN_CHARACTER_NAME`![await][page]\n I heard you left and threw down with `SEASIDE_BOSS`![await]\n The Shymores on lookout saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n They got the good stuff from `FINAL_BOSS_NAME`[await]\n We’d better get back aboard before any other Shymore party fouls. I heard Exor might even show up![await][page]\n\n                             Hang loose!\n                               Claymorton[await]""",
        DI2061_HEAD_CHEF: """BODYGUARD: Doesn’t this cake\n look just like Claymorton?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Claymorton must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CLAYMORTON: I’m not happy to\n delay the party, but we can’t get\n started until you get 4 more items![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Claymorton’s busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Claymorton.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CLAYMORTON:\n[center]What’re YOU doing here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Claymorton’s\n house up on the hill yet?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CLAYMORTON: Think you’re gonna\n beat the dojo master today?[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CLAYMORTON: I guess you CAN\n bounce after all.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CLAYMORTON: I guess you CAN\n bounce after all.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BODYGUARD: Think you’re tough,\n pal?[await][delay] March that ugly mustache into\n Mack’s room, and see what\n happens![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BODYGUARD: You beat Mack?[await]\n This is not good![delay_30]\n I guess you can bounce after all.[await]""",
        DI2560_TOWER_HENCHMAN_1: """BODYGUARD: Welcome![await][pause]\n Our party is invitation-only, so\n please come back another time.[await][page]\n[delay] ...You’re here to crash it anyway?[delay]\n Alright, wise guy, let’s go![await]""",
        DI2572_TOWER_HENCHMAN_2: """\n   BODYGUARD: Oh, no you don’t![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """BODYGUARD: I almost feel bad\n for all those fools out there,\n who can’t even bounce...[await]""",
        DI3073_TOWER_HENCHMAN_3: """BODYGUARD: How ’bout a fat lip to\n go with that ugly moustache?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BODYGUARD: Think you’re tough,\n pal?[await][delay] March that ugly mustache into\n Claymorton’s room, and see what\n happens![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BODYGUARD: You beat Claymorton?[await]\n This is not good![delay_30]\n I guess you can bounce after all.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Mack’s busy right now, so he can’t\n play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Mack.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            KeroSewersGate, KeroSewersGating.MACK
        ):
            output.extend(
                [
                    ClearBit(SEWERS_CLOSED),
                    RemoveObjectFromSpecificLevel(NPC_0, R333_KERO_SEWERS_ENTRANCE),
                    RemoveObjectFromSpecificLevel(NPC_1, R333_KERO_SEWERS_ENTRANCE),
                ]
            )
        return EventScript(output)


__all__ = ["MackBossFight"]
