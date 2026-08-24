from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_moleville_postgame_boss, can_damage_enemies_with_spells, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerMinesPostgameBossFight(BossFightLocation):
    _bias = True
    _originally_held = Punchinello2BossFight
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _default_battlefield = BF25_UNDERGROUND
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _pack_id = PACK071_MINES_POSTGAME
    _post_unlocks_event_id = E1253_POSTGAME_MINES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
            NPC_0,
        ),
    ]
    _access_conditions = "Must first defeat the boss fight at inner Moleville and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_postgame_boss(world, inventory)


__all__ = ["InnerMinesPostgameBossFight"]
