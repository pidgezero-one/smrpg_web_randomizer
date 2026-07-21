from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_ship_postgame_boss)
from randomizer.progression.prizelocations.access import (can_access_ship_postgame_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2, NPC_3, NPC_4)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipPostgameBossFight(BossFightLocation):
    _bias = True
    _originally_held = Johnny2Fight
    _rooms = [R003_POSTGAME_SHIP]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 526
    _default_battlefield = BF04_SUNKEN_SHIP
    _remake_only = True
    _pack_id = PACK118_SHIP_POSTGAME
    _post_unlocks_event_id = E1209_POSTGAME_SHIP_END_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R003_POSTGAME_SHIP,
            NPC_0,
            sequence_setter_event_id=E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_2],
        ),
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_3],
        ),
        BossFightLocationHenchmanNPC(
            [R003_POSTGAME_SHIP],
            [NPC_4],
        ),
    ]
    _dialogs_expecting_replacement = [
        DI2023_SHIP_BOSS_2_DRINK,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        assert self.prize is not None
        op = super().render(world)
        render_ship_postgame_boss(world, self.prize)
        return op


__all__ = ["ShipPostgameBossFight"]
