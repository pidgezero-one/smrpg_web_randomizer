from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_forest_maze_character, render_forest_maze_character_empty)
from randomizer.progression.prizelocations.access import (can_clear_forest, is_all_starting_chars_set)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (AllyNPCSub, CharacterRecruitmentLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_11)
from randomizer.data.rooms.npcs import MARIO_ENDING_2
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ForestMazeCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = GenoRecruitmentPrize
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_CHARACTER
    _world_area = WorldAreaEnum.FOREST_MAZE
    _container_event = E1226_FOREST_MAZE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            NPC_11,
        ),
        AllyNPCSub(
            R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            NPC_10,
        ),
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 91),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitSet(FOREST_LIBERATED, ["next"]),
        Jmp(["forest_maze_hint_text"]),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(6)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.prize is None:
            render_forest_maze_character_empty(world)
        else:
            assert isinstance(self.prize, CharacterPrize)
            self._apply_forest_maze_npc_overrides(world)
            render_forest_maze_character(world, self.prize)
        return op

    def _apply_forest_maze_npc_overrides(self, world: GameWorld) -> None:
        """Use the MARIO_ENDING_2 (sprite 0) NPC for Mario at every forest-maze fill.

        Forest-maze animations apply sprite_offset relative to sprite 0
        (because render_forest_maze_character passes use_primary=True for
        Mario). The default MarioCharacterNPC base is sprite 409, which makes
        those offsets resolve to unrelated sprites and corrupts animation.
        """
        assert isinstance(self.prize, CharacterPrize)
        if not isinstance(self.prize, MarioRecruitmentPrize):
            return

        for npc_sub in self._npc_fills:
            room = world.rooms._rooms[npc_sub.room_id]
            if room is None:
                continue
            obj = room.get_npc_by_target_id(npc_sub.npc_id)
            if obj is not None:
                obj._npc = MARIO_ENDING_2


__all__ = ["ForestMazeCharacter"]
