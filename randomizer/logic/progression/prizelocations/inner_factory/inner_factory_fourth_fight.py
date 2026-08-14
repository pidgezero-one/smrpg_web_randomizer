from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4, NPC_5)
from randomizer.logic.progression.prizelocations.access import (can_access_factory, can_damage_enemies_with_spells, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_12)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_inner_factory_fourth_fight(world: GameWorld) -> None:
    """Hide NPCs 0-6 in Gun Yolk's room for non-vanilla boss."""
    room = world.rooms._rooms[R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    assert (
        room is not None
    ), f"Room {R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM} not found"
    for npc_id in [NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6]:
        obj = room.get_npc_by_target_id(npc_id)
        assert (
            obj is not None
        ), f"NPC {npc_id} not found in room {R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM}"
        obj.set_visible(False)


class InnerFactoryFourthFight(BossFightLocation):
    _bias = True
    _originally_held = GunyolkBossFight
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_4
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK149_FACTORY_BOSS_RUSH_4
    _post_unlocks_event_id = E1244_INNER_FACTORY_4_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            NPC_12,
            sequence_setter_event_id=E0858_INNER_FACTORY_4TH_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        # If the prize is not the original GunyolkBossFight, hide NPCs 0-6 in room 470
        if not isinstance(self.prize, GunyolkBossFight):
            render_inner_factory_fourth_fight(world)
        return op

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)


__all__ = ["InnerFactoryFourthFight"]
