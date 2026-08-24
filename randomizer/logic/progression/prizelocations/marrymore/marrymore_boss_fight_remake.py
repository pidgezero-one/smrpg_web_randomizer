from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_chapel_postgame_boss, can_damage_enemies_with_spells, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarrymoreBossFightRemake(BossFightLocation):
    _bias = True
    _originally_held = Bundt2BossFight
    _rooms = [R050_POSTGAME_CHAPEL]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.MARRYMORE
    _override_id = 529
    _default_battlefield = BF35_MARRYMORE_CHAPEL_SANCTUARY
    _remake_only = True
    _pack_id = PACK078_CHAPEL_POSTGAME
    _post_unlocks_event_id = E1258_POST_CHAPEL_POSTGAME_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R050_POSTGAME_CHAPEL,
            NPC_0,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R050_POSTGAME_CHAPEL],
            [NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [R050_POSTGAME_CHAPEL],
            [NPC_2],
        ),
    ]
    _access_conditions = "Must first defeat the boss fight at Marrymore and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."


    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel_postgame_boss(world, inventory)

    def render(self, world: GameWorld):
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        is_vanilla = isinstance(self.prize, (BundtBossFight, Bundt2BossFight))
        has_henchmen_substitutions = (
            self.prize.character_henchmen is not None
            and len(self.prize.character_henchmen) > 0
        ) or (
            self.prize.mook_henchmen is not None and len(self.prize.mook_henchmen) > 0
        )
        if not is_vanilla and not has_henchmen_substitutions:
            room = world.rooms._rooms[R050_POSTGAME_CHAPEL]
            assert room is not None
            room.get_npc_by_target_id(NPC_1).set_visible(False)
            room.get_npc_by_target_id(NPC_2).set_visible(False)
        return op


__all__ = ["MarrymoreBossFightRemake"]
