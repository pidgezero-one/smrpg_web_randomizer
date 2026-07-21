from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_lands_end)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow4, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_9)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BelomeTempleRMLChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_4
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 264),
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
            NPC_9, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)
    
    def render(self, world: GameWorld) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)
        world.overworld_dialogs.replace_dialog(
            DI1248_FORTUNE_6, self.prize.fortune_type if self.prize is not None else FortuneEnum.YIKES
        )
        return op


__all__ = ["BelomeTempleRMLChestLocation"]
