from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (boss_slot_min_vram_cap_for_room, can_damage_enemies_with_spells)
from randomizer.progression.prizelocations.mushroom_way.mushroom_way_character import MushroomWayCharacter
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_7)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def _mushroom_way_boss_min_vram_cap(world: GameWorld) -> int:
    return boss_slot_min_vram_cap_for_room(
        world,
        R205_MUSHROOM_WAY_AREA_03,
        base_budget=1,
        recruit_location=MushroomWayCharacter,
    )


class MushrooomWayBossFight(BossFightLocation):
    _originally_held = HammerBrosFight
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_BOSS_FIGHT
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _pack_id = PACK183_MUSHROOM_WAY_BOSS
    _post_unlocks_event_id = E1194_MUSHROOM_WAY_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R205_MUSHROOM_WAY_AREA_03,
            NPC_7,
            sequence_setter_event_id=E0755_MUSHROOM_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER,
            # Cap shuffled bosses based on what else is in the room this seed.
            # Room 205 has 3 cannot_clone NPCs (Toad/Lakitu/HammerBro) plus the
            # Spikey buffer; ally_buffer and the recruit slot both grow when
            # Bowser is involved, eating into NPC 7's safe budget.
            vram_size_override=2048,
            min_vram_size_override=_mushroom_way_boss_min_vram_cap,
            min_vram_from_seq0_override=_mushroom_way_boss_min_vram_cap,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MUSHROOM_WAY):
            content.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])


__all__ = ["MushrooomWayBossFight"]
