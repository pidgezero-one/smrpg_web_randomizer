from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_nimbus_boss, can_damage_enemies_with_spells, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_11, NPC_12, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_9)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class NimbusFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = ValentinaBossFight
    _rooms = [R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_FINAL_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK171_NIMBUS_CASTLE_THIRD_BOSS
    _post_unlocks_event_id = E1232_NIMBUS_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA,
            NPC_9,
            sequence_setter_event_id=E0822_NIMBUS_LAND_OCCUPIED_EXTERIOR_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            NPC_4,
            sequence_setter_event_id=E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_9,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            ],
            [NPC_11],
        ),
        BossFightLocationHenchmanNPC(
            [
                R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            ],
            [NPC_12],
        ),
    ]
    _statue_slots = [
        # Garro's house
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_1,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_2,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_3,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Main hall
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_0,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_1,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_2,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_3,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_4,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_5,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Occupied 4-way path
        BossFightLocationNPC(
            R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Antechamber
        BossFightLocationNPC(
            R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            NPC_0,
            sequence_setter_event_id=E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            NPC_1,
            sequence_setter_event_id=E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Occupied throne room
        BossFightLocationNPC(
            R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0826_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0826_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Polishing room
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_0,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_1,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_2,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Lone statue room
        BossFightLocationNPC(
            R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            NPC_3,
            sequence_setter_event_id=E0827_NIMBUS_CASTLE_SINGLE_BIRD_STATUE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Left shaman hall
        BossFightLocationNPC(
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            NPC_6,
            sequence_setter_event_id=E0829_NIMBUS_CASTLE_EARLY_WEST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            NPC_7,
            sequence_setter_event_id=E0829_NIMBUS_CASTLE_EARLY_WEST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Right shaman hall
        BossFightLocationNPC(
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM,
            NPC_6,
            sequence_setter_event_id=E0830_NIMBUS_CASTLE_EARLY_EAST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM,
            NPC_7,
            sequence_setter_event_id=E0830_NIMBUS_CASTLE_EARLY_EAST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Liberated throne room
        BossFightLocationNPC(
            R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0831_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0831_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Hot springs
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_1,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_2,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_3,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_4,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Cellar hallway
        BossFightLocationNPC(
            R497_NIMBUS_CASTLE_AREA_06_DUMMY,
            NPC_0,
            sequence_setter_event_id=E0834_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R497_NIMBUS_CASTLE_AREA_06_DUMMY,
            NPC_1,
            sequence_setter_event_id=E0834_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Five-door hallway
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_2,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_3,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_4,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Liberated 4-way path
        BossFightLocationNPC(
            R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0836_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0836_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI1120_NIMBUS_BIRD_GUARD,
        DI1945_NIMBUS_GUARD,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
            content.extend(
                [
                    SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                    SetBit(MAP_BARREL_VOLCANO),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])


__all__ = ["NimbusFinalBossFight"]
