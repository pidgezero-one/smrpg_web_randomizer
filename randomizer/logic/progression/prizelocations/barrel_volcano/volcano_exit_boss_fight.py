from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.overworld_area_names import (OW50_BARREL_VOLCANO)
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_StartLoopNTimes)
from randomizer.logic.progression.prizelocations.access import (can_clear_volcano, can_damage_enemies_with_spells, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, RemoveIfNotFilled, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
from uuid import (uuid4)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_volcano_exit_boss(
    world: GameWorld,
    prize: BossFightPrize,
) -> None:
    """Apply henchman slot event script changes for Volcano Exit boss fight."""

    def slot_has_henchman(slot_index: int) -> bool:
        return (
            prize.character_henchmen is not None
            and len(prize.character_henchmen) > slot_index
        )

    loops = 0

    # Slot 0 - black
    if not slot_has_henchman(0):
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq_2")
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq_3")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_1
        ).set_visible(False)
        world.get_room(R391_VOLCANO_POSTCD_AREA_04).get_npc_by_target_id(
            NPC_0
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_2).set_visible(False)
    else:
        loops += 1

    # Slot 1 - pink
    if not slot_has_henchman(1):
        world.event_scripts.delete_command_by_identifier("axem_henchman_2_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_2_aq_2")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_2
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_3).set_visible(False)
    else:
        loops += 1

    # Slot 2 - green
    if not slot_has_henchman(2):
        world.event_scripts.delete_command_by_identifier("axem_henchman_3_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_3_aq_2")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_3
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_4).set_visible(False)
        world.get_room(R394_VOLCANO_POSTCD_AREA_05).get_npc_by_target_id(
            NPC_1
        ).set_visible(False)
    else:
        loops += 1

    # Slot 3 - yellow
    if not slot_has_henchman(3):
        world.event_scripts.delete_command_by_identifier("axem_henchman_4_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_4_aq_2")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_4
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_5).set_visible(False)
        world.get_room(R394_VOLCANO_POSTCD_AREA_05).get_npc_by_target_id(
            NPC_0
        ).set_visible(False)
    else:
        loops += 1

    if loops == 0:
        world.event_scripts.delete_subscript_command_by_identifier("axem_trampoline_aqueue", "axem_trampoline_loop")
        world.event_scripts.delete_subscript_command_by_identifier("axem_trampoline_aqueue", "axem_trampoline_endloop")
    else:
        # Get the loop command and set its count (don't delete it)
        world.event_scripts.get_subscript_command_by_identifier(
            "axem_trampoline_aqueue",
            "axem_trampoline_loop",
            A_StartLoopNTimes,
        ).set_count(loops)


class VolcanoExitBossFight(BossFightLocation):
    _bias = True
    _originally_held = AxemRangersBossFight
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _pack_id = PACK182_VOLCANO_BOSS
    _post_unlocks_event_id = E1234_VOLCANO_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R392_VOLCANO_POSTCD_AREA_06,
            NPC_0,
            sequence_setter_event_id=E0842_VOLCANO_FINAL_PRE_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R394_VOLCANO_POSTCD_AREA_05,
            NPC_2,
            sequence_setter_event_id=E0843_VOLCANO_POST_BOSS_ROOM_WITH_ENEMY_WARPS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            NPC_1,
            sequence_setter_event_id=E0844_VOLCANO_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R391_VOLCANO_POSTCD_AREA_04,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_1, NPC_0, NPC_2],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_2, NPC_3],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                R394_VOLCANO_POSTCD_AREA_05,
            ],
            [NPC_3, NPC_4, NPC_1],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R394_VOLCANO_POSTCD_AREA_05,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_4, NPC_0, NPC_5],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_volcano(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.VOLCANO):
            content.extend(
                [
                    SetBit(MAP_VISTA_HILL),
                    ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
                ]
            )
            if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                content.extend(
                    [
                        SetBit(MAP_GATE),
                        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                    ]
                )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        # STAR_PIECE_TRIGGER_EVENT
        op = super().render(world)
        if self.prize is None:
            identifier = str(uuid4())
            first: list[list[UsableEventScriptCommand]] = [
                [
                    JmpIfVarEqualsConst(
                        PRIMARY_TEMP_7000,
                        R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                        [identifier],
                    )
                ]
            ]
            second: list[UsableEventScriptCommand] = [
                ExitToWorldMap(area=OW50_BARREL_VOLCANO, bit_6=True, bit_7=True),
                Return(),
            ]
            op = (first, second, op[2])
        if isinstance(self.prize, AxemRangersBossFight):
            return op
        assert isinstance(self.prize, BossFightPrize)
        render_volcano_exit_boss(world, self.prize)
        return op


__all__ = ["VolcanoExitBossFight"]
