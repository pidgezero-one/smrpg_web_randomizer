from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_tower)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, StandardPrizeLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerFallingChestLocation(
    NPCLocationRow1
):  # this looks like a chest, requires an overworld item, but acts like a npc reward
    _originally_held = MasherPrize
    _rooms = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_MASHER
    _container_event = E0253_NPC_QUEST_1_GRANT
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 141),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_SEESAW_CHEST_OPENED, ["next"]),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        # This spot renders like a chest, so it's the one NPC/event location allowed to hold
        # YouMissed — which only defines a chest_grant, no npc_grant. Skip EventLocation's
        # npc_grant gate for it (every other NPC location still rejects it), keep base gating.
        if isinstance(prize, YouMissed):
            return StandardPrizeLocation.can_accept(self, prize, inventory, world)
        return super().can_accept(prize, inventory, world)

    def grant(self, world: GameWorld | None = None) -> EventScript:
        # In AnnoyingChests mode an empty falling chest still plays the "You Missed"
        # animation, so fill it with YouMissed (rendered via its masher-chest chest_grant).
        prize = self.prize
        if (
            prize is None
            and world is not None
            and world.settings.isflag_enabled(AnnoyingChests)
        ):
            self.set_prize(YouMissed())
            prize = self.prize
        # Any YouMissed here renders via its chest_grant (masher variant), not npc_grant.
        if isinstance(prize, YouMissed):
            prize._masher_chest = True
            return prize.chest_grant
        return super().grant(world)

    def render(self, world: GameWorld) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)
        if self.prize is None:
            if not world.settings.isflag_enabled(AnnoyingChests):
                world.event_2496_startup += [
                    DisableObjectTriggerInSpecificLevel(NPC_0, R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER),
                    SetBit(TOWER_SEESAW_CHEST_OPENED),
                ]
        return op


__all__ = ["BoosterTowerFallingChestLocation"]
