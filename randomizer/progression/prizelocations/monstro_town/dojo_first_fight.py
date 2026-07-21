from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_dojo_first_fight)
from randomizer.progression.prizelocations.access import (can_access_monstro_town, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class DojoFirstFight(BossFightLocation):
    _bias = True
    _originally_held = JaggerBossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _pack_id = PACK189_DOJO_PREFIGHT
    _post_unlocks_event_id = E1213_DOJO_1_BOSS_UNLOCKS
    _allow_run_away = True

    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_1,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 289),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        render_dojo_first_fight(world, self.prize)
        return op


__all__ = ["DojoFirstFight"]
