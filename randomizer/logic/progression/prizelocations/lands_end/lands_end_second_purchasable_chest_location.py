from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_lands_end)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_19)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndSecondPurchasableChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = LandsEndStar3Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_3
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [SlotsPrize] 
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 257),
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
            NPC_19, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)
        
    def render(self, world: GameWorld) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)
        if self.prize is None and not world.settings.isflag_enabled(AnnoyingChests):
            world.event_scripts.replace_command_by_identifier("floating_chest_2_lands_end_underground", SetBit(LANDS_END_CHEST_2_USED))
        return op


__all__ = ["LandsEndSecondPurchasableChestLocation"]
