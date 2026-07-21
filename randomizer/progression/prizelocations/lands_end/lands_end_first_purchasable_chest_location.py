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
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_18)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndFirstPurchasableChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndStar2Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_2
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [FirstMimicFightLauncher, SecondMimicFightLauncher, InfiniteCoinsPrize, SlotsPrize] # no reloadables
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 256),
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
            NPC_18, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)
        
    def render(self, world: GameWorld) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)
        if self.prize is None and not world.settings.isflag_enabled(AnnoyingChests):
            world.event_scripts.replace_command_by_identifier("floating_chest_1_lands_end_underground", SetBit(LANDS_END_CHEST_1_USED))
        return op


__all__ = ["LandsEndFirstPurchasableChestLocation"]
