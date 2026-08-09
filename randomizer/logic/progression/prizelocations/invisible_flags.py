from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_access_bandits_way, can_access_chapel, can_access_factory, can_access_forest, can_access_lands_end, can_access_moleville_entrance, can_access_monstro_town, can_access_nimbus_castle, can_access_outer_nimbus, can_access_pipe_vault, can_access_sea, can_access_sewer, can_access_tower, can_access_volcano, can_clear_chapel, can_clear_forest, can_clear_mines, can_clear_nimbus_boss, can_clear_seaside_boss, can_clear_ship, can_pass_obstacle_courses, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (InvisibleFlagLocation, PrizeLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_3, NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MariosPadBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 3
    _y_coord = 11
    _world_area = WorldAreaEnum.MARIOS_PAD
    _clue_text = """[center]My item's underneath a green bed.[await]"""
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 440),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) or world.settings.isflag_enabled(SkipMustyFearsSequence)


class RoseTownSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 10
    _y_coord = 47
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = """[center]My item's behind a wooden flower.[await]"""
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 441),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) or world.settings.isflag_enabled(SkipMustyFearsSequence)


class YosterIsleGoalFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R034_YOSTER_ISLE]
    _x_coord = 21
    _y_coord = 62
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _y_shift = -4
    _clue_text = """[center]My item's between "O" and "A".[await]"""
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 442),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory) and (
            can_access_monstro_town(world, inventory)
            or world.settings.isflag_enabled(SkipMustyFearsSequence)
        )


class MariosPadSteamwhistleFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R016_MARIOS_PAD]
    _x_coord = 11
    _y_coord = 34
    _world_area = WorldAreaEnum.MARIOS_PAD
    _z_coord = 1
    _clue_text = "[center]Mine is underneath a steamwhistle.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 443),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    # All other flag locations are in logic only after you can talk to the musty fears because otherwise how tf would you know where to look?
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MariosPadLanternFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R016_MARIOS_PAD]
    _x_coord = 13
    _y_coord = 35
    _world_area = WorldAreaEnum.MARIOS_PAD
    _x_shift = 8
    _y_shift = -8
    _clue_text = "[center]Mine is under a white lantern.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 444),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MariosPadHatFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 5
    _y_coord = 13
    _world_area = WorldAreaEnum.MARIOS_PAD
    _z_coord = 1
    _clue_text = """[center]My item's under a red hat.[await]"""
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 445),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomWayTreeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _x_coord = 11
    _y_coord = 16
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _z_coord = 3
    _x_shift = -16
    _clue_text = " Mine's under a tree, up on a ledge\n by itself.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 446),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomKingdomSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _x_coord = 22
    _y_coord = 116
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _z_coord = 2
    _y_shift = -8
    _clue_text = "[center]Mine's behind a wooden mushroom.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 447),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomKingdomEmptyHouseFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R482_MUSHROOM_KINGDOM_DURING_MACK_RAZ_AND_RAINIS_HOUSE,
        R490_MUSHROOM_KINGDOM_RAZ_AND_RAINIS_HOUSE,
    ]
    _x_coord = 14
    _y_coord = 61
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _y_shift = 8
    _clue_text = " Mine is under the bed in an empty\n house.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 448),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class ChancellorThroneFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
        R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
    ]
    _x_coord = 19
    _y_coord = 24
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _z_coord = 3
    _clue_text = "[center]Mine's under a blue chair.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 449),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BanditsWayFlowerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _x_coord = 25
    _y_coord = 89
    _world_area = WorldAreaEnum.BANDITS_WAY
    _x_shift = 16
    _clue_text = "[center]Mine's on a landing flower.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 450),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_bandits_way(
            world, inventory
        )


class KeroStairsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _x_coord = 5
    _y_coord = 41
    _world_area = WorldAreaEnum.KERO_SEWERS
    _x_shift = -4
    _clue_text = " Mine's in a corner, nearby lots of\n dank stairs.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 451),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(SEWERS_CLOSED, ["ks_availability_check"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="ks_availability_check"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sewer(
            world, inventory
        )


class KeroGateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE]
    _x_coord = 4
    _y_coord = 88
    _world_area = WorldAreaEnum.KERO_SEWERS
    _z_coord = 4
    _x_shift = -16
    _clue_text = "[center]Mine is by a lone metal spike fence.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 452),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(SEWERS_CLOSED, ["ks_availability_check_2"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="ks_availability_check_2"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sewer(
            world, inventory
        )


class MidasTreesFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _x_coord = 24
    _y_coord = 26
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _x_shift = -8
    _clue_text = " Mine's between a lone pair of\n palm trees, near the water.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 453),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class TadpoleCabinetFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _x_coord = 25
    _y_coord = 29
    _world_area = WorldAreaEnum.TADPOLE_POND
    _z_coord = 2
    _x_shift = 4
    _clue_text = "[center]Mine is in a frog cabinet.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 454),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseWayDirtPatchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    _x_coord = 25
    _y_coord = 88
    _world_area = WorldAreaEnum.ROSE_WAY
    _clue_text = " Mine is in the middle of a HUGE\n patch of dirt.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 455),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 15
    _y_coord = 63
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = -8
    _clue_text = "[center]Mine is under a depressed hydrant.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 456),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownSinkFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R089_ROSE_TOWN_DURING_BOWYER_THREE_GRANDKIDS_HOUSE,
        R090_ROSE_TOWN_THREE_GRANDKIDS_HOUSE,
    ]
    _x_coord = 15
    _y_coord = 10
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = 1
    _clue_text = "[center]My item is in a kitchen sink under\n[center] some green curtains.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 457),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownBowserFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R085_ROSE_TOWN_DURING_BOWYER_INN_1F,
        R086_ROSE_TOWN_INN_1F,
    ]
    _x_coord = 7
    _y_coord = 21
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = "[center]Mine's under a tiny turtle.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 458),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownGardenerHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 2
    _y_coord = 85
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = -8
    _clue_text = "[center]Mine is under a private hydrant.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 459),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class RoseTownGardenerBucketFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 5
    _y_coord = 87
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = "[center]Mine is under a private bucket.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 460),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class RoseTownGardenerLeafFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _x_coord = 4
    _y_coord = 111
    _world_area = WorldAreaEnum.ROSE_TOWN
    _z_coord = 10
    _clue_text = "[center]Mine's on a big leaf between\n[center] two chests.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 461),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["rose_town_cloud_invisible_hint_check"]),
        JmpIfBitSet(GAVE_SEED, ["hint_check_fertilizer3"]),
        StoreItemAmountTo7000(SeedItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            GAVE_FERTILIZER,
            ["rose_town_cloud_invisible_hint_check"],
            identifier="hint_check_fertilizer3",
        ),
        StoreItemAmountTo7000(FertilizerItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED,
            ["next"],
            identifier="rose_town_cloud_invisible_hint_check",
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class ForestMazeSecretStumpFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R231_FOREST_MAZE_SECRET_ENTRANCE]
    _x_coord = 18
    _y_coord = 72
    _world_area = WorldAreaEnum.FOREST_MAZE
    _x_shift = 16
    _clue_text = " Mine is behind a brightly\n illuminated tree stump.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 462),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class ForestMazeSecretMushroomsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R235_FOREST_MAZE_AREA_08_UNDERGROUND]
    _x_coord = 24
    _y_coord = 93
    _world_area = WorldAreaEnum.FOREST_MAZE
    _y_shift = 8
    _clue_text = " Mine is on an illuminated pack of\n 5 mushrooms.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 463),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class ForestMazeSecretWigglerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER]
    _x_coord = 2
    _y_coord = 39
    _world_area = WorldAreaEnum.FOREST_MAZE
    _clue_text = "[center]Mine is on a sleepy bug.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 464),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class PipeVaultExteriorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R055_PIPE_VAULT_ENTRANCE]
    _x_coord = 17
    _y_coord = 19
    _world_area = WorldAreaEnum.PIPE_VAULT
    _x_shift = -12
    _clue_text = " Mine is by a pipe in the middle of\n the road.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 465),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class PipeVaultRedPipeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R129_PIPE_VAULT_AREA_05]
    _x_coord = 21
    _y_coord = 107
    _world_area = WorldAreaEnum.PIPE_VAULT
    _x_shift = -8
    _y_shift = 8
    _clue_text = "[center]Mine is behind a low red pipe.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 466),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class YosterIsleHutFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R034_YOSTER_ISLE]
    _x_coord = 11
    _y_coord = 70
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _clue_text = "[center]Mine's under a fruity gazebo.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 467),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class MolevilleHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 6
    _y_coord = 63
    _world_area = WorldAreaEnum.MOLEVILLE
    _y_shift = -8
    _clue_text = "[center]Mine's under a gold hydrant.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 468),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMountainBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 19
    _y_coord = 33
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 14
    _clue_text = " Mine's in a bush at the top of\n a mountain.[await]"
    _y_shift = 8
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 469),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMountainGoFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 21
    _y_coord = 39
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 12
    _clue_text = " Mine is on “GO”.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1009),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R337_MOLEVILLE_INN]
    _x_coord = 6
    _y_coord = 12
    _world_area = WorldAreaEnum.MOLEVILLE
    _x_shift = 16
    _clue_text = "[center]Mine's under a middle bed.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 470),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMinesArrowsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _x_coord = 5
    _y_coord = 51
    _world_area = WorldAreaEnum.MOLEVILLE
    _clue_text = " Mine's between two arrows pointing away from each other.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 471),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) and can_access_moleville_entrance(world, inventory)


class MolevilleMinesCeilingFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    _x_coord = 8
    _y_coord = 13
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 4
    _clue_text = " Mine's in a zig-zag room, up\n on the ceiling.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 472),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) and can_access_moleville_entrance(world, inventory)


class MolevilleMinesEntryFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING]
    _x_coord = 22
    _y_coord = 23
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 3
    _x_shift = 16
    _clue_text = " My item?[delay]\n ...[delay]It's on the word “IN”,\n [delay]above a long track.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 473),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_mines(
            world, inventory
        )


class BoosterPassCornerBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _x_coord = 17
    _y_coord = 112
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _x_shift = -8
    _y_shift = 8
    _clue_text = "[center]Mine's in a corner bush.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 474),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BoosterTowerExteriorSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _x_coord = 4
    _y_coord = 110
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = " Mine's behind a sign with Japanese\n letters.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 475),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BoosterTowerDeskFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM]
    _x_coord = 24
    _y_coord = 113
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = '\n      Mine\'s under "B" and "K".[await]'
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 476),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_1"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_1"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerMasherRoomFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _x_coord = 19
    _y_coord = 122
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _y_shift = -8
    _clue_text = "[center]Mine's on a lightly-loaded see-saw.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 477),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_2"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_2"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerCurtainFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    _x_coord = 7
    _y_coord = 64
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _z_coord = 9
    _y_shift = 8
    _clue_text = " Mine's in a corner, between a window and a solid red curtain.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 478),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_3"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_3"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerThwompInvisibleFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER]
    _x_coord = 5
    _y_coord = 114
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _z_coord = 12
    _clue_text = "[center]Mine is near a lonely thwomp.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 479),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_4"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_4"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerBrokenFrameFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    _x_coord = 15
    _y_coord = 83
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = -8
    _y_shift = -9
    _clue_text = "[center]Mine is in a broken frame.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 480),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_5"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_5"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerBeetleCageFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 18
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _clue_text = "[center]Mine is on an insect cage.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 481),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_6"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_6"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerToyBoxFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 24
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 8
    _clue_text = "[center]Mine is behind a toy box.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 482),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["tower_invis_check_7"]),
        JmpIfBitClear(TOWER_CHARACTER_RECRUITED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"], "tower_invis_check_7"),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class MarrymoreOutsideCrateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
        R064_MARRYMORE_OUTSIDE,
    ]
    _x_coord = 23
    _y_coord = 60
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = "[center]Mine is under a lone backyard box.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 483),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreHallwayFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R011_MARRYMORE_INN_3F]
    _x_coord = 18
    _y_coord = 76
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 3
    _clue_text = " My item is in a flower pot in a\n hallway.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 484),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreCurtains(InvisibleFlagLocation):
    _bias = True
    _rooms = [R012_MARRYMORE_INN_SUITE_ROOM]
    _x_coord = 5
    _y_coord = 12
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 0
    _x_shift = -8
    _clue_text = " Mine's beneath a clock. The clock is beside some red plaid curtains.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1008),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreSuiteBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R012_MARRYMORE_INN_SUITE_ROOM]
    _x_coord = 7
    _y_coord = 13
    _world_area = WorldAreaEnum.MARRYMORE
    _x_shift = -16
    _clue_text = " Mine's beneath two adjoined\n red beds.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 485),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreKitchenFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R155_MARRYMORE_CHAPEL_KITCHEN]
    _x_coord = 2
    _y_coord = 20
    _world_area = WorldAreaEnum.MARRYMORE
    _x_shift = -8
    _clue_text = " Mine is in a big cabinet full of\n dishes.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 486),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreFireplaceFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R152_MARRYMORE_CHAPEL_MAIN_HALL]
    _x_coord = 9
    _y_coord = 33
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 2
    _x_shift = 8
    _clue_text = "[center]Mine is in an empty fireplace.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 487),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreWindowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY,
    ]
    _x_coord = 17
    _y_coord = 15
    _y_shift = -8
    _world_area = WorldAreaEnum.MARRYMORE
    _clue_text = " Mine is under a single stained glass window.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1007),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class MarrymoreOrganFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
        R294_MARRYMORE_CHAPEL_CLONE_BOSS_LAUNCHER
    ]
    _x_coord = 23
    _y_coord = 65
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine is behind a big musical\n instrument.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 488),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class MarrymoreAltarFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
        R294_MARRYMORE_CHAPEL_CLONE_BOSS_LAUNCHER
    ]
    _x_coord = 23
    _y_coord = 70
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 1
    _clue_text = "[center]Mine's behind a podium.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 489),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class StarHillNorthStarFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R158_STAR_HILL_AREA_02]
    _x_coord = 8
    _y_coord = 69
    _world_area = WorldAreaEnum.STAR_HILL
    _z_coord = 2
    _x_shift = -10
    _clue_text = "[center]Mine is atop the North Star.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 490),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownAnchorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 14
    _y_coord = 57
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _x_shift = 16
    _clue_text = "[center]Mine is behind an anchor.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 491),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 16
    _y_coord = 25
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _z_coord = 5
    _x_shift = 0
    _y_shift = -8
    _clue_text = "[center]Mine is under a high steel hydrant.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 492),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownBucketFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 20
    _y_coord = 31
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _y_shift = 8
    _z_coord = 3
    _clue_text = "[center]Mine is in a bucket between two\n[center]staircases.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 493),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownFlowersFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
        R313_SEASIDE_TOWN_ACCESSORY_SHOP,
    ]
    _x_coord = 26
    _y_coord = 60
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _y_shift = -8
    _x_shift = -8
    _clue_text = " Mine's in the middle of three\n pink flowers.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 494),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownShedBoxFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _x_coord = 5
    _y_coord = 23
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _y_shift = 8
    _clue_text = " Mine's under a lone crate in an\n empty house.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 495),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["seaside_town_invis_check"]),
        JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            ["seaside_town_invis_check"],
        ),
        StoreItemAmountTo7000(ShedKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="seaside_town_invis_check"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_seaside_boss(world, inventory)
            and inventory.has_item(ShedKeyPrize)
        )


class SeaArrowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 8
    _y_coord = 21
    _world_area = WorldAreaEnum.SEA
    _x_shift = -8
    _y_shift = -8
    _clue_text = "[center]Mine is beside a mossy up-arrow.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 496),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaBoxesFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 9
    _y_coord = 36
    _world_area = WorldAreaEnum.SEA
    _y_shift = 8
    _clue_text = "[center]Mine's in some V-shaped boxes.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 497),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaStalagnateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _x_coord = 18
    _y_coord = 43
    _world_area = WorldAreaEnum.SEA
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is behind a big gray\n stalagnate.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 498),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaUnderwaterSailFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R174_SEA_AREA_08_SHORE_WITH_SUNKEN_SHIP]
    _x_coord = 4
    _y_coord = 41
    _world_area = WorldAreaEnum.SEA
    _clue_text = "[center]Mine's behind a sail.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 499),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipBarrelPileFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES]
    _x_coord = 7
    _y_coord = 66
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _z_coord = 3
    _clue_text = "[center]Mine is atop a big pile of barrels.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 500),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipDoorMarkerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY]
    _x_coord = 18
    _y_coord = 82
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _z_coord = 1
    _y_shift = 8
    _clue_text = " Mine is on a stack of boxes.[await][pause]\n[delay] Hm?[delay] Is that not specific enough?[await][page]\n Well,[delay] the boxes act as a door\n marker.[delay] They represent the\n number “4”.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 501),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipButtonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _x_coord = 16
    _y_coord = 113
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _clue_text = "[center]Mine is under a floating button.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 502),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipSwitchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _x_coord = 17
    _y_coord = 121
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _clue_text = (
        'Mine is underneath a floating "J"\n[center]that is all on its lonesome.[await]'
    )
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 503),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_ship(
            world, inventory
        )


class LandsEndPlatformFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R137_LANDS_END_AREA_01]
    _x_coord = 6
    _y_coord = 29
    _world_area = WorldAreaEnum.LANDS_END
    _clue_text = "[center]Mine is under a rising platform.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 504),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class LandsEndCannonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL]
    _x_coord = 11
    _y_coord = 115
    _world_area = WorldAreaEnum.LANDS_END
    _y_shift = -8
    _clue_text = " Mine's inside a big, quiet cannon.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 505),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndArrowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _x_coord = 28
    _y_coord = 29
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 16
    _clue_text = "[center]Mine is beside an orange up-arrow.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 506),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndHillFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R404_LANDS_END_DESERT_AREA_04]
    _x_coord = 23
    _y_coord = 96
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 8
    _y_shift = 8
    _clue_text = " Mine is on a short, remote red hill.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 507),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndTwoHillFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R319_LANDS_END_DESERT_AREA_06]
    _x_coord = 8
    _y_coord = 121
    _world_area = WorldAreaEnum.LANDS_END
    _clue_text = "   My item's between two red hills.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 508),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndStalagmiteFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R265_LANDS_END_UNDERGROUND_AREA_03]
    _x_coord = 22
    _y_coord = 88
    _z_coord = 4
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = -8
    _y_shift = -8
    _clue_text = (
        " Mine's on a big stalagmite\n formation in an underground cave.[await]"
    )
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 509),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndCliffBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 23
    _y_coord = 103
    _world_area = WorldAreaEnum.LANDS_END
    _z_coord = 22
    _clue_text = " Mine is on a bush, way up high on\n a cliff.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 510),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 24
    _y_coord = 118
    _world_area = WorldAreaEnum.LANDS_END
    _z_coord = 0
    _y_shift = -4
    _x_shift = 8
    _clue_text = "[center]My item's on a yellow arrow.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 511),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class TempleShaftFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM]
    _x_coord = 22
    _y_coord = 56
    _world_area = WorldAreaEnum.TEMPLE
    _x_shift = 8
    _clue_text = " My item's in an elevator shaft.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1004),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class TempleShaftSwitchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM]
    _x_coord = 17
    _y_coord = 18
    _world_area = WorldAreaEnum.TEMPLE
    _z_coord = 2
    _x_shift = 8
    _clue_text = " My item's below one golden wall ornament.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1005),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class DojoBonsaiFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _x_coord = 6
    _y_coord = 9
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _x_shift = -8
    _clue_text = "[center]Mine's underneath a bonsai tree.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 512),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroEntranceSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _x_coord = 9
    _y_coord = 102
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _clue_text = "[center]Mine's in a lone flowery bush.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 513),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroBatFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _x_coord = 5
    _y_coord = 51
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 4
    _x_shift = -8
    _clue_text = "[center]Mine's behind a wooden bat.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 514),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroFanFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R395_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_1F]
    _x_coord = 12
    _y_coord = 80
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 1
    _x_shift = -16
    _clue_text = "[center]Mine's beside a fan.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 515),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroShellFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP]
    _x_coord = 16
    _y_coord = 15
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 1
    _y_shift = -8
    _clue_text = "[center]Mine's beneath a spinning shell.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 516),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyPipeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _x_coord = 17
    _y_coord = 85
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine's on an isolated, dead-end\n pipe.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 517),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyBeanstalkBlockFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA]
    _x_coord = 27
    _y_coord = 27
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _clue_text = "[center]Mine's underneath a big beanstalk.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 518),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyCloudsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _x_coord = 18
    _y_coord = 70
    _z_coord = 1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _clue_text = "Mine is below a long red spiral.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1010),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class CasinoBellFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _x_coord = 5
    _y_coord = 20
    _z_coord = 1
    _world_area = WorldAreaEnum.CASINO
    _x_shift = -4
    _y_shift = -4
    _clue_text = "[center]Mine is beside a tiny bell.[await][pause]\n[center]I don't think it does anything.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 519),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        StoreItemAmountTo7000(BrightCardItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            BrightCardPrize
        )


class NimbusGoldGoombaFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R341_NIMBUS_LAND_GARROS_HOUSE]
    _x_coord = 5
    _y_coord = 14
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 1
    _clue_text = "[center]Mine is on a golden Goomba.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 520),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusOutdoorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
        R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
    ]
    _x_coord = 5
    _y_coord = 49
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 2
    _clue_text = "My item is under a tree star.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1011),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusInnLobbyFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R343_NIMBUS_LAND_INN]
    _x_coord = 6
    _y_coord = 84
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 2
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is under a stove with two\n pots.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 521),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusPlantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT
    ]
    _x_coord = 27
    _y_coord = 74
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 1
    _clue_text = " Mine is behind a big potted plant\n in a corner.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 522),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_10"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_10"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="nimbus_ck_dummy_10"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_nimbus_castle(
            world, inventory
        )


class NimbusBirdFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _x_coord = 28
    _y_coord = 48
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _y_shift = 8
    _x_shift = -8
    _clue_text = " Mine is under a birdcage, in a\n restricted dead-end area.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 523),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_ck_dummy_11"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_ck_dummy_11"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["nimbus_ck_dummy2_11"],
            identifier="nimbus_ck_dummy_11",
        ),
        StoreItemAmountTo7000(CastleKey1Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["nimbus_ck_dummy3_11"],
            identifier="nimbus_ck_dummy2_11",
        ),
        StoreItemAmountTo7000(CastleKey2Item),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="nimbus_ck_dummy3_11"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_nimbus_boss(
            world, inventory
        )


class NimbusHotSpringsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R447_NIMBUS_LAND_HOT_SPRINGS]
    _x_coord = 19
    _y_coord = 114
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 5
    _clue_text = " Mine's on the right side of a\n hot pool.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 524),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(
            INVISIBLE_ITEMS_SUMMONED, ["next"], identifier="nimbus_ck_dummy3_12"
        ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_nimbus_boss(
            world, inventory
        )


class BarrelVolcanoInnSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP]
    _x_coord = 15
    _y_coord = 106
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 6
    _clue_text = (
        "\n My item?[await]\n It's on an “INN” that's missing its second “N”.[await]"
    )
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1000),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class BarrelVolcanoStumpetFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R390_VOLCANO_AREA_16_ERUPTING_STUMPET]
    _x_coord = 15
    _y_coord = 8
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 0
    _clue_text = (
        "\n Mine is behind a big tree. A BIIIIIG tree. It doesn't have leaves.[await]"
    )
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1002),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class VolcanoShipsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 11
    _y_coord = 61
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 2
    _clue_text = "[center]Mine is between two vehicles.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 525),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class VolcanoBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 8
    _y_coord = 56
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 1
    _x_shift = 8
    _clue_text = "[center]Mine is on a firm mattress.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1001),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class VolcanoLampFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 6
    _y_coord = 56
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 0
    _clue_text = (
        " Mine is under the only artificial light source in the volcano.[await]"
    )
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1003),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class KeepPostObstacleBossRoomFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _x_coord = 26
    _y_coord = 97
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _x_shift = 8
    _clue_text = "[center]Mine is between two red doors.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 526),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_pass_obstacle_courses(world, inventory)
            and not_earlygame(world, inventory)
        )


class KeepThwompFlag(InvisibleFlagLocation):
    _bias = True 
    _rooms = [R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM]
    _x_coord = 19
    _y_coord = 47
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _clue_text = "[center]Mine is under a big thwomp.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 527),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_pass_obstacle_courses(world, inventory)
            and not_earlygame(world, inventory)
        )


class FactoryLugnutFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _x_coord = 23
    _y_coord = 50
    _world_area = WorldAreaEnum.FACTORY
    _z_coord = 7
    _clue_text = "    My item's underneath a lugnut.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 529),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_factory(
            world, inventory
        )


class FactoryTrampolineFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN]
    _x_coord = 14
    _y_coord = 9
    _world_area = WorldAreaEnum.FACTORY
    _y_shift = 8
    _clue_text = " My item is with the world's\n loneliest trampoline.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 530),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )


class FactoryButtonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _x_coord = 4
    _y_coord = 36
    _world_area = WorldAreaEnum.INNER_FACTORY
    _z_coord = 5
    _clue_text = " Mine is on a jammed machine\n button.[await]"
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 531),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["invisible_item_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )


class ThreeMustyFearsBonesProxy(PrizeLocation):
    """Proxy class for Dry Bones' invisible item slot in Three Musty Fears."""

    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS_BONES


class ThreeMustyFearsGreaperProxy(PrizeLocation):
    """Proxy class for Greaper's invisible item slot in Three Musty Fears."""

    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS_GREAPER


class ThreeMustyFearsBooProxy(PrizeLocation):
    """Proxy class for Big Boo's invisible item slot in Three Musty Fears."""

    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS_BOO


__all__ = [
    "MariosPadBedFlag",
    "RoseTownSignFlag",
    "YosterIsleGoalFlag",
    "MariosPadSteamwhistleFlag",
    "MariosPadLanternFlag",
    "MariosPadHatFlag",
    "MushroomWayTreeFlag",
    "MushroomKingdomSignFlag",
    "MushroomKingdomEmptyHouseFlag",
    "ChancellorThroneFlag",
    "BanditsWayFlowerFlag",
    "KeroStairsFlag",
    "KeroGateFlag",
    "MidasTreesFlag",
    "TadpoleCabinetFlag",
    "RoseWayDirtPatchFlag",
    "RoseTownHydrantFlag",
    "RoseTownSinkFlag",
    "RoseTownBowserFlag",
    "RoseTownGardenerHydrantFlag",
    "RoseTownGardenerBucketFlag",
    "RoseTownGardenerLeafFlag",
    "ForestMazeSecretStumpFlag",
    "ForestMazeSecretMushroomsFlag",
    "ForestMazeSecretWigglerFlag",
    "PipeVaultExteriorFlag",
    "PipeVaultRedPipeFlag",
    "YosterIsleHutFlag",
    "MolevilleHydrantFlag",
    "MolevilleMountainBushFlag",
    "MolevilleMountainGoFlag",
    "MolevilleBedFlag",
    "MolevilleMinesArrowsFlag",
    "MolevilleMinesCeilingFlag",
    "MolevilleMinesEntryFlag",
    "BoosterPassCornerBushFlag",
    "BoosterTowerExteriorSignFlag",
    "BoosterTowerDeskFlag",
    "BoosterTowerMasherRoomFlag",
    "BoosterTowerCurtainFlag",
    "BoosterTowerThwompInvisibleFlag",
    "BoosterTowerBrokenFrameFlag",
    "BoosterTowerBeetleCageFlag",
    "BoosterTowerToyBoxFlag",
    "MarrymoreOutsideCrateFlag",
    "MarrymoreHallwayFlag",
    "MarrymoreCurtains",
    "MarrymoreSuiteBedFlag",
    "MarrymoreKitchenFlag",
    "MarrymoreFireplaceFlag",
    "MarrymoreWindowFlag",
    "MarrymoreOrganFlag",
    "MarrymoreAltarFlag",
    "StarHillNorthStarFlag",
    "SeasideTownAnchorFlag",
    "SeasideTownHydrantFlag",
    "SeasideTownBucketFlag",
    "SeasideTownFlowersFlag",
    "SeasideTownShedBoxFlag",
    "SeaArrowFlag",
    "SeaBoxesFlag",
    "SeaStalagnateFlag",
    "SeaUnderwaterSailFlag",
    "ShipBarrelPileFlag",
    "ShipDoorMarkerFlag",
    "ShipButtonFlag",
    "ShipSwitchFlag",
    "LandsEndPlatformFlag",
    "LandsEndCannonFlag",
    "LandsEndArrowFlag",
    "LandsEndHillFlag",
    "LandsEndTwoHillFlag",
    "LandsEndStalagmiteFlag",
    "LandsEndCliffBushFlag",
    "LandsEndSignFlag",
    "TempleShaftFlag",
    "TempleShaftSwitchFlag",
    "DojoBonsaiFlag",
    "MonstroEntranceSignFlag",
    "MonstroBatFlag",
    "MonstroFanFlag",
    "MonstroShellFlag",
    "BeanValleyPipeFlag",
    "BeanValleyBeanstalkBlockFlag",
    "BeanValleyCloudsFlag",
    "CasinoBellFlag",
    "NimbusGoldGoombaFlag",
    "NimbusOutdoorFlag",
    "NimbusInnLobbyFlag",
    "NimbusPlantFlag",
    "NimbusBirdFlag",
    "NimbusHotSpringsFlag",
    "BarrelVolcanoInnSignFlag",
    "BarrelVolcanoStumpetFlag",
    "VolcanoShipsFlag",
    "VolcanoBedFlag",
    "VolcanoLampFlag",
    "KeepPostObstacleBossRoomFlag",
    "KeepThwompFlag",
    "FactoryLugnutFlag",
    "FactoryTrampolineFlag",
    "FactoryButtonFlag",
    "ThreeMustyFearsBonesProxy",
    "ThreeMustyFearsGreaperProxy",
    "ThreeMustyFearsBooProxy",
]
