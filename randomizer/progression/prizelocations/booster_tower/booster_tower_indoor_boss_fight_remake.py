from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_booster_tower_indoor_boss_postgame)
from randomizer.progression.prizelocations.access import (can_access_tower_postgame_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2, NPC_3)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerIndoorBossFightRemake(BossFightLocation):
    _bias = True
    _originally_held = Booster2BossFight
    _rooms = [R004_POSTGAME_TOWER]
    _override_id = 528
    _default_battlefield = BF12_BOOSTER_TOWER
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _pack_id = PACK070_TOWER_POSTGAME
    _post_unlocks_event_id = E1202_POSTGAME_TOWER_CURTAIN_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R004_POSTGAME_TOWER,
            NPC_0,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R004_POSTGAME_TOWER],
            [NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [R004_POSTGAME_TOWER],
            [NPC_2],
        ),
        BossFightLocationHenchmanNPC(
            [R004_POSTGAME_TOWER],
            [NPC_3],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)

    def render(self, world: GameWorld):
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if self.npc_slots and self.prize and self.prize.model:
            render_booster_tower_indoor_boss_postgame(
                world,
                self.prize,
            )
        assert isinstance(self.prize, BossFightPrize)
        is_vanilla = isinstance(self.prize, (BoosterBossFight, Booster2BossFight))
        has_henchmen_substitutions = (
            self.prize.character_henchmen is not None
            and len(self.prize.character_henchmen) > 0
        ) or (
            self.prize.mook_henchmen is not None and len(self.prize.mook_henchmen) > 0
        )
        if not is_vanilla and not has_henchmen_substitutions:
            room = world.rooms._rooms[R004_POSTGAME_TOWER]
            assert room is not None
            room.get_npc_by_target_id(NPC_1).set_visible(False)
            room.get_npc_by_target_id(NPC_2).set_visible(False)
            room.get_npc_by_target_id(NPC_3).set_visible(False)

        return op


__all__ = ["BoosterTowerIndoorBossFightRemake"]
