from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_sealed_postgame_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroSealedDoorBossFightPostgame(BossFightLocation):
    _bias = True
    _originally_held = Culex3DBossFight
    _rooms = [R351_CULEXS_ROOM]
    _override_id = 524
    _default_battlefield = BF47_CULEX
    _id = ShuffleLocationSelector.CULEX_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _pack_id = PACK055_MONSTRO_DOOR_POSTGAME
    _post_unlocks_event_id = E1219_POSTGAME_MONSTRO_SEALED_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_postgame_boss(world, inventory)
    
    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (CulexBossFight, Culex3DBossFight, MokuraBossFight, KnifeGuyGrateGuyBossFight, KingCalamariBossFight, MegasmilaxBossFight, CzarDragonBossFight)
        ):
            world.event_scripts.delete_command_by_identifier("sealed_boss_2_seq_loop_on")
        return op

    _dialogs_expecting_replacement = [DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT]


__all__ = ["MonstroSealedDoorBossFightPostgame"]
