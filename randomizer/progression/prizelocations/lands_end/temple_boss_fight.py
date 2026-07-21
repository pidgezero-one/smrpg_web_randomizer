from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_clear_temple_boss, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TempleBossFight(BossFightLocation):
    _bias = True
    _originally_held = Belome2BossFight
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_FIGHT
    _world_area = WorldAreaEnum.TEMPLE
    _pack_id = PACK169_TEMPLE_BOSS
    _post_unlocks_event_id = E1211_TEMPLE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            NPC_4,
            sequence_setter_event_id=E0814_TEMPLE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.LANDS_END):
            content.extend(
                [
                    SetBit(MAP_MONSTRO_TOWN),
                    SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_temple_boss(world, inventory)


__all__ = ["TempleBossFight"]
