from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_inner_factory_fourth_fight)
from randomizer.data.rooms.npcs import (EMPTY_NPC_3)
from randomizer.progression.prizelocations.access import (can_access_factory, can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_12, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerFactoryFourthFight(BossFightLocation):
    _bias = True
    _originally_held = GunyolkBossFight
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_4
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK149_FACTORY_BOSS_RUSH_4
    _post_unlocks_event_id = E1244_INNER_FACTORY_4_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            NPC_12,
            sequence_setter_event_id=E0858_INNER_FACTORY_4TH_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            ],
            [NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6],
        ),
    ]

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        # If the prize is not the original GunyolkBossFight, hide NPCs 0-6 in room 470
        if not isinstance(self.prize, GunyolkBossFight):
            render_inner_factory_fourth_fight(world)
        return op

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        # Base class only calls this when the prize isn't GunyolkBossFight.
        # Room 470's NPCs 0-6 are Gunyolk-specific set dressing that render()
        # hides anyway, so blank them regardless of whether the incoming boss
        # supplied henchmen — otherwise an unrendered henchman model stays
        # loaded in those slots and gets budgeted VRAM.
        if self._character_henchman_slots is None:
            return
        for slot in self._character_henchman_slots:
            for room_id, npc_id in zip(slot.room_ids, slot.npc_ids):
                room = world.rooms._rooms[room_id]
                assert room is not None, f"Room {room_id} not found"
                obj = room.get_npc_by_target_id(npc_id)
                assert obj is not None, f"NPC {npc_id} not found in room {room_id}"
                obj._npc = EMPTY_NPC_3
                if self._chosen_henchman_models_by_room_npc is not None:
                    self._chosen_henchman_models_by_room_npc.pop(
                        (room_id, int(npc_id)), None
                    )

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)


__all__ = ["InnerFactoryFourthFight"]
