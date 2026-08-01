from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow3, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import (AreaObject)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Mimic1ReloadRewardLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = Coins50Prize
    _rooms: list[int] = []  # Dynamic room, handled by mimic system
    _npc_ids: list[AreaObject] = []  # No specific NPC
    _id = ShuffleLocationSelector.PANDORITE_REWARD_2
    _world_area = WorldAreaEnum.KERO_SEWERS
    _override_id = 512
    # FirstMimicFightLauncher must be blacklisted to prevent circular dependency:
    # This location's can_access requires defeating first mimic, which requires
    # accessing the FirstMimicFightLauncher location - can't be the same location.
    _blacklist = [EXPStarPrize, SlotsPrize, MimicFightInitiatorPrize, InfiniteCoinsPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    def grant(self, world: GameWorld | None = None) -> EventScript:
        # Mimic rewards don't need room-specific chest disable commands
        if self.prize is None and not world.settings.isflag_enabled(AnnoyingChests):
            return EventScript([Return()])
        return EventScript(
            [] if self.prize.chest_grant is None else self.prize.chest_grant.contents
        )


__all__ = ["Mimic1ReloadRewardLocation"]
