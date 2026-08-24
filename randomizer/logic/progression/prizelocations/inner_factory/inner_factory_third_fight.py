from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (NORMAL)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_Pause, A_SetSequenceSpeed, A_SetSpriteSequence)
from randomizer.logic.progression.prizelocations.access import (can_access_factory, can_damage_enemies_with_spells, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_defeat_factory_bosses)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (BossFightHenchman, Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_7, NPC_8, NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_inner_factory_third_fight_slot(
    world: GameWorld,
    henchman: BossFightHenchman,
    slot_index: int,
) -> None:
    """Apply factory pierce animation for a single henchman slot."""
    anim = henchman.model().animations.factory_pierce

    slot_configs = [
        (
            A0962_FACTORY_3RD_BOSS_LEFT_HAMMER,
            "factory_3rd_boss_left_hammer_attack",
            "factory_3rd_boss_left_hammer_attack_pause_32",
        ),
        (
            A0963_FACTORY_3RD_BOSS_MID_HAMMER,
            "factory_3rd_boss_mid_hammer_attack",
            "factory_3rd_boss_mid_hammer_attack_pause_32",
        ),
        (
            A0964_FACTORY_3RD_BOSS_RIGHT_HAMMER,
            "factory_3rd_boss_right_hammer_attack",
            "factory_3rd_boss_right_hammer_attack_pause_32",
        ),
    ]

    if slot_index >= len(slot_configs):
        return

    script_id, attack_id, pause_id = slot_configs[slot_index]

    if (
        anim is not None
        and anim.contact_frame is not None
    ):
        prepause = 32 - anim.total_duration
        world.action_scripts.get_command_by_identifier(
            attack_id, A_SetSpriteSequence
        ).set_index(anim.sequence_id)
        world.action_scripts.get_command_by_identifier(pause_id, A_Pause).set_length(
            anim.contact_frame
        )
        if anim.speed is not NORMAL:
            world.action_scripts.scripts[script_id].insert_before_identifier(
                attack_id, A_SetSequenceSpeed(anim.speed)
            )
        if prepause != 0:
            world.action_scripts.scripts[script_id].insert_before_identifier(
                attack_id, A_Pause(prepause)
            )
    else:
        world.action_scripts.delete_command_by_identifier(attack_id)


class InnerFactoryThirdFight(BossFightLocation):
    _bias = True
    _originally_held = DirectorBossFight
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK148_FACTORY_BOSS_RUSH_3
    _post_unlocks_event_id = E1243_INNER_FACTORY_3_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R472_FACTORY_GROUNDS_AREA_03,
            NPC_10,
            sequence_setter_event_id=E0857_INNER_FACTORY_3RD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_7]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_8]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_9]),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_defeat_factory_bosses(world, inventory)

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        # Read the resolved assignments, not prize.character_henchmen: bosses with
        # only _mook_henchmen (Count Down) get their character slots backfilled with
        # mooks by the base class, and never populate character_henchmen.
        by_slot = dict(henchmen_assignments)
        for slot_index, slot in enumerate(self._character_henchman_slots or []):
            henchman = by_slot.get(slot)
            if henchman is not None:
                render_inner_factory_third_fight_slot(world, henchman, slot_index)


__all__ = ["InnerFactoryThirdFight"]
