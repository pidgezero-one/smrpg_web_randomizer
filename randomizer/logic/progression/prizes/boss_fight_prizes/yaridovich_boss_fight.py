from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.enemies.enemies import (DRILLBITEnemy, YARIDOVICHEnemy, YARIDOVICHMirageEnemy)
from randomizer.data.packs.pack_collection import (FORM0290_ONE_YARIDOVICH_ONE_YARIDOVICHMIRAGE)
from randomizer.data.physical_objects.bosses import (YaridOverworldObject, YaridovichLargeObject, YaridovichSmallObject, YaridovichStatueObject)
from randomizer.data.physical_objects.henchmen import (DrillbitHenchman)
from randomizer.data.variables.dialog_names import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
    DI1120_NIMBUS_BIRD_GUARD,
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
    DI1945_NIMBUS_GUARD,
    DI2023_SHIP_BOSS_2_DRINK,
    DI2061_HEAD_CHEF,
    DI2062_APPRENTICE_CHEF,
    DI2180_CHAPEL_NPC,
    DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
    DI2560_TOWER_HENCHMAN_1,
    DI2572_TOWER_HENCHMAN_2,
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
from randomizer.data.variables.variable_names import (LANDS_END_GATED)
from randomizer.types.prize import (BossFightHenchman, BossFightPrize)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (FormationMember)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (ClearBit)
from randomizer.types.flags import (LandsEndGate, LandsEndGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)
    from randomizer.types.prizelocation import (BossFightLocation)
    from randomizer.types.physical_objects import (BossNPC)


class YaridovichBossFight(BossFightPrize):
    _text = "Yaridovich"
    _formation = FORM0290_ONE_YARIDOVICH_ONE_YARIDOVICHMIRAGE
    _members = [
        FormationMember(YARIDOVICHEnemy, 183, 127),
        FormationMember(YARIDOVICHMirageEnemy, 183, 127, hidden_at_start=True),
    ]
    _anchor_enemy = YARIDOVICHEnemy
    _hp_slice_excluded_enemies = [YARIDOVICHMirageEnemy]
    _additional_enemies_to_scale = [DRILLBITEnemy]

    _seaside_letter_name_if_seaside_boss = "Yarid"
    _seaside_letter_name_if_seaside_boss_remake = "Speary"
    _seaside_letter_name_if_volcano_boss = "some conspicuous toads circling"
    _seaside_letter_name_if_final_boss = "Yaridovich's spies."
    _seaside_letter_name_if_final_boss_remake = "Speardovich's spies."
    _remake_name = "Speardovich"

    _npc_models = [YaridovichLargeObject, YaridOverworldObject, YaridovichSmallObject]
    _statue_npc = YaridovichStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=DRILLBITEnemy, model=DrillbitHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """YARIDOVICH: How could I lose to\n those...[delay] Huh? Hey, get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eee hee hee! So, you’ve cracked the\n code... Now, it’s time for the\n REAL test![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Yaridovich’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n YARIDOVICH!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """YARIDOVICH: Ridiculous! How could\n a genius like me lose to them...?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """YARIDOVICH: I’m thinking it might\n be time for me to switch careers.[await][page]\n Say, do you happen to know anyone\n who’s looking to hire a\n hydrodemolitions expert?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """YARIDOVICH: This is just adding\n insult to injury![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """VILLAGER: We must.. be\n careful. We could rust.. down here.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,[await][page]\n By now, you’ve certainly defeated `SEASIDE_BOSS`, I think.[await]\n My “Toad” spies tell me they saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I suspect they’re one of `FINAL_BOSS_NAME`[await]\n Give’em “the Tickler” from me![await]\n My joints are starting to rust, so I’ll be headin’ back down.[await]\n Stop by whenever you need something unsavory, okay?[await][page]\n\n                   Your confidant,\n                         Yaridovich[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """VILLAGER: Hop on... the\n trampoline... in the next room.\n It’ll take you... outside.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """VILLAGER: We must.. be\n careful. We could rust.. down here.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ My disguise was as see-through[await]\n as this glass of Motor Oil!![await]""",
        DI2023_SHIP_BOSS_2_DRINK: """ My disguise was as see-through[await]\n as this glass of Motor Oil!![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """VILLAGER: We must.. be\n careful. We could rust.. down here.[await]""",
        DI2061_HEAD_CHEF: """VILLAGER: We must... make\n this cake... look exactly...\n like Yaridovich.[await]""",
        DI2062_APPRENTICE_CHEF: """VILLAGER:\n[center]We need... more fondant.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Yaridovich must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """YARIDOVICH: Eee hee...! You’re\n still missing a few things. They\n should be in this room.[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """YARIDOVICH: Finally! You found all\n the gear![await][page]\n Now make yourself useful and pick\n up the rest of the trash in this\n room![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Yaridovich is busy right now, so he\n can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Yaridovich.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """YARIDOVICH: A challenge from the\n dojo master? [delay]Eee hee hee, this\n ought to be interesting![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eee hee...! You want to fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Eee hee...! You want to fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It’s really weird.\n Sometimes I hear the guy next door.[await][page]\n He’s always mumbling about\n Brownie-this and Tickle-that.[await][page]\n Sometimes I’d like to ask him what\n he’s babbling about, but the door\n won’t open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """YARIDOVICH: I guess I wasn’t as\n strong as I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """YARIDOVICH: I guess I wasn’t as\n strong as I thought...[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """\n There’s nothing...to see...in here.[await]""",
        DI1945_NIMBUS_GUARD: """ If you have...no business...please\n leave.[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """SPEARDOVICH: How could I lose to\n those...[delay] Huh? Hey, get lost![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You’re pretty tough, `MAIN_CHARACTER_MOLE_GREETING`. All right. I’ll let you through to Speardovich’s place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That’s AMAZING!\n No one’s EVER whipped\n SPEARDOVICH!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """SPEARDOVICH: Ridiculous! How\n could a genius like me lose to\n them...?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """SPEARDOVICH: I’m thinking it might\n be time for me to switch careers.[await][page]\n Say, do you happen to know anyone\n who’s looking to hire a\n hydrodemolitions expert?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """SPEARDOVICH: This is just adding\n insult to injury![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,[await][page]\n By now, you’ve certainly defeated `SEASIDE_BOSS`, I think.[await]\n My “Toad” spies tell me they saw `VOLCANO_BOSS_DESCRIPTION` near the volcano.[await]\n I suspect they’re one of `FINAL_BOSS_NAME`[await]\n Give’em “the Tickler” from me![await]\n My joints are starting to rust, so I’ll be headin’ back down.[await]\n Stop by whenever you need something unsavory, okay?[await][page]\n\n                   Your confidant,\n                        Speardovich[await]""",
        DI2061_HEAD_CHEF: """VILLAGER: We must... make\n this cake... look exactly...\n like Speardovich.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Speardovich must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """SPEARDOVICH: Eee hee...! You’re\n still missing [0x7024] item(s)! Isn’t that\n a shame?[await]""",
        DI4060_NEED_TO_DO_CHAPEL_CHECKS: """SPEARDOVICH: Finally! You found\n all the gear![await][page]\n Now make yourself useful and pick\n up the rest of the trash in this\n room![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Speardovich is busy right now, so\n he can’t play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Speardovich.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """SPEARDOVICH: A challenge from the\n dojo master? [delay]Eee hee hee, this\n ought to be interesting![await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """SPEARDOVICH: I guess I wasn’t as\n strong as I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """SPEARDOVICH: I guess I wasn’t as\n strong as I thought...[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """VILLAGER: Well done...\n You may go on... to Yaridovich.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """VILLAGER: You won...\n Well done...[await]""",
        DI2560_TOWER_HENCHMAN_1: """VILLAGER: I’m just... a\n secretary. Don’t bother...\n Yaridovich.[await]""",
        DI2572_TOWER_HENCHMAN_2: """VILLAGER: This is...not...\n the right way.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """VILLAGER: It’s nice...\n outside.[await]""",
        DI3073_TOWER_HENCHMAN_3: """VILLAGER: You want...to\n fight?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """VILLAGER: Well done...\n You may go on... to Speardovich.[await]""",
        DI2560_TOWER_HENCHMAN_1: """VILLAGER: I’m just... a\n secretary. Don’t bother...\n Speardovich.[await]""",
    }

    def get_forced_npc_model_for_location(
        self, location: "BossFightLocation"
    ) -> type[BossNPC] | None:
        # In the Nimbus Land statue room the larger Yaridovich overworld model
        # doesn't render correctly, so pin the smallest model there.
        from randomizer.logic.progression.prizelocations import (StatueRoomBossFight)

        if isinstance(location, StatueRoomBossFight):
            return YaridovichSmallObject
        return None

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            LandsEndGate, LandsEndGating.YARIDOVICH
        ):
            output.extend([ClearBit(LANDS_END_GATED)])
        return EventScript(output)


__all__ = ["YaridovichBossFight"]
