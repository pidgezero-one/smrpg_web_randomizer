from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_tower, can_damage_enemies_with_spells, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerBalconyBossFight(BossFightLocation):
    _bias = True
    _originally_held = KnifeGuyGrateGuyBossFight
    _rooms = [R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _pack_id = PACK177_TOWER_SECOND_BOSS
    _post_unlocks_event_id = E1203_TOWER_BALCONY_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.TOWER):
            content.extend([ClearBit(BOOSTER_HILL_CLOSED)])
        if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
            content.extend([SetBit(MARRYMORE_BACKDOOR_OPEN)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])


__all__ = ["BoosterTowerBalconyBossFight"]
