from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_sealed_door_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroSealedDoorBossFight(BossFightLocation):
    _bias = True
    _originally_held = CulexBossFight
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_BOSS_FIGHT
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _pack_id = PACK216_MONSTRO_DOOR_BOSS
    _post_unlocks_event_id = E1218_MONSTRO_SEALED_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI3338_MONSTRO_SUPERBOSS_HINT,
        DI3057_MONSTRO_SUPERBOSS_PROMPT,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_door_boss(world, inventory)

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
            world.event_scripts.delete_command_by_identifier("sealed_boss_1_seq_loop_on")
        return op


__all__ = ["MonstroSealedDoorBossFight"]
