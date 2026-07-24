from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_final_boss_conveyor_lackeys, render_final_boss_fight)
from randomizer.progression.prizelocations.access import (can_access_inner_factory_final_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_10, NPC_11, NPC_15, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class FinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = SmithyBossFight
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_FINAL
    _world_area = WorldAreaEnum.INNER_FACTORY
    _rooms = [R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, R509_FACTORY_GROUNDS_SMITHYS_PAD]
    _pack_id = PACK185_FINAL_BOSS
    _force_battlefield = BF44_FACTORY_GROUNDS_SMITHYS_PAD
    _post_unlocks_event_id = E1245_INNER_FACTORY_5_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R509_FACTORY_GROUNDS_SMITHYS_PAD,
            NPC_8,
            sequence_setter_event_id=E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
            ],
            [
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_15,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
            ],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_factory_final_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, SmithyBossFight):
            render_final_boss_fight(world, self.prize)
        mook = self.get_chosen_henchman_model_for_slot(
            R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, NPC_7
        )
        if mook is not None:
            render_final_boss_conveyor_lackeys(world, mook)
        return op


__all__ = ["FinalBossFight"]
