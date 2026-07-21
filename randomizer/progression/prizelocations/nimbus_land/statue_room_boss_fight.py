from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_statue_room_boss)
from randomizer.progression.prizelocations.access import (can_access_nimbus_castle, can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_3)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class StatueRoomBossFight(BossFightLocation):
    _bias = True
    _originally_held = DodoBossFight
    _override_id = 520
    _default_battlefield = BF22_NIMBUS_CASTLE
    _id = ShuffleLocationSelector.NIMBUS_LAND_STATUE_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK208_NIMBUS_CASTLE_FIRST_BOSS
    _post_unlocks_event_id = E1230_STATUE_BOSS_UNLOCKS
    _rooms = [
        R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
        R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
    ]
    _npc_slots = [
        BossFightLocationNPC(
            R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            NPC_1,
            sequence_setter_event_id=E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_3,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationNPC(
            R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI2180_CHAPEL_NPC]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)

        assert self._npc_slots is not None
        statue_slot = next(
            (
                s
                for s in self._npc_slots
                if s.room_id == R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM
            ),
            None,
        )
        chosen = (
            self.resolve_npc_model_for_slot(world, statue_slot)
            if statue_slot is not None
            else None
        )
        render_statue_room_boss(
            world,
            self.prize,
            world.settings.isflag_enabled(KeepMinigameSpritesIntact),
            chosen_npc_model=chosen,
        )
        return op


__all__ = ["StatueRoomBossFight"]
