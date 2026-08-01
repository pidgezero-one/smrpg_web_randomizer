from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_SetSpriteSequence)
from randomizer.logic.progression.prizelocations.access import (is_all_starting_chars_set)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (AllyNPCSub, CharacterRecruitmentLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_5, NPC_7, NPC_8)
from randomizer.data.rooms.npcs import MARIO_ENDING_2
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_mushroom_way_character(world: GameWorld, prize: CharacterPrize | None) -> None:
    if prize is None:
        world.event_scripts.delete_subscript_command_by_identifier(
            "EVENT_1710_mario_mad_slot1_aq", "EVENT_1710_mario_mad_slot1"
        )
    else:
        ally_index = prize.ally.index
        if ally_index == 0:
            cmd = world.event_scripts.get_subscript_command_by_identifier(
                "EVENT_1710_mario_mad_slot1_aq", "EVENT_1710_mario_mad_slot1", A_SetSpriteSequence
            )
            cmd.set_index(3)
            cmd.set_sprite_offset(3)


class MushroomWayCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = MallowRecruitmentPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_CHARACTER
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _container_event = E1225_MUSHROOM_WAY_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(R203_MUSHROOM_WAY_AREA_01, NPC_8),
        AllyNPCSub(R204_MUSHROOM_WAY_AREA_02, NPC_7),
        AllyNPCSub(R205_MUSHROOM_WAY_AREA_03, NPC_5),
        AllyNPCSub(R206_BANDITS_WAY_AREA_05, NPC_10),
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 11),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return is_all_starting_chars_set(world, inventory)

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(2)
        return super().set_prize(prize)

    def render(self, world: GameWorld):
        op = super().render(world)
        self._apply_room206_npc_override(world)
        if self.prize is not None:
            assert isinstance(self.prize, CharacterPrize)
        render_mushroom_way_character(world, self.prize)
        return op

    def _apply_room206_npc_override(self, world: GameWorld) -> None:
        """Use the MARIO_ENDING_2 (sprite 0) NPC for Mario at the room 206 fill.

        The default MarioCharacterNPC base is sprite 409 (the Mario clone
        monster sprite), which the base CharacterRecruitmentLocation.render
        assigns to every fill. For the room 206 (Bandits Way area 5) NPC 10
        slot we want the real protagonist sprite 0 instead.
        """
        if not isinstance(self.prize, MarioRecruitmentPrize):
            return

        room = world.rooms._rooms[R206_BANDITS_WAY_AREA_05]
        if room is None:
            return
        obj = room.get_npc_by_target_id(NPC_10)
        if obj is not None:
            obj._npc = MARIO_ENDING_2


__all__ = ["MushroomWayCharacter"]
