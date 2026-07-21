from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.renders import (render_marrymore_character, render_marrymore_character_empty)
from randomizer.progression.prizelocations.access import (can_clear_chapel, is_all_starting_chars_set)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (AllyNPCSub, CharacterRecruitmentLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_8)
from smrpgpatchbuilder.datatypes.levels.classes import BufferType
from randomizer.data.rooms.npcs import MARIO_ENDING_2
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarrymoreCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = ToadstoolRecruitmentPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_CHARACTER
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E1228_MARRYMORE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_10,
        ),
        AllyNPCSub(
            R054_BOOSTER_HILL_DUMMY,
            NPC_8,
        ),
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 201),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["marrymore_hint_text"]),
        StoreItemAmountTo7000(RingItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(CrownItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(ShoesItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(BroochItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(9)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.prize is None:
            render_marrymore_character_empty(world)
        else:
            assert isinstance(
                self.prize, CharacterPrize
            ), f"MarrymoreCharacter prize must be CharacterPrize, got {type(self.prize)}"
            self._apply_marrymore_npc_overrides(world)
            render_marrymore_character(world, self.prize)
        return op

    def _apply_marrymore_npc_overrides(self, world: GameWorld) -> None:
        """Apply per-character NPC overrides for Marrymore chapel/Booster Hill.

        Mario: every fill (chapel NPC_10 and Booster Hill NPC_8) gets the
        MARIO_ENDING_2 (sprite 0) NPC. Chapel animations are driven by
        update_ally_animation with use_primary=True, so the sprite_offsets
        are relative to sprite 0; leaving any fill at the default sprite 409
        Mario clone makes those offsets resolve to wrong sprites and corrupts
        the chapel animation.

        Bowser is cannot_clone=True with vram_size=1 (dedicated VRAM).
        All others are cloneable (cannot_clone=False, vram_size=0).
        """

        assert isinstance(self.prize, CharacterPrize)

        if isinstance(self.prize, MarioRecruitmentPrize):

            for npc_sub in self._npc_fills:
                room = world.rooms._rooms[npc_sub.room_id]
                if room is None:
                    continue
                obj = room.get_npc_by_target_id(npc_sub.npc_id)
                if obj is not None:
                    obj._npc = MARIO_ENDING_2

        room_54 = world.rooms._rooms[R054_BOOSTER_HILL_DUMMY]
        if room_54 is None:
            return

        # Apply NPC 8 vram/clone tuning in room 54 (Booster Hill).
        obj = room_54.get_npc_by_target_id(NPC_8)
        if obj is None:
            return
        if isinstance(self.prize, BowserRecruitmentPrize):
            obj._min_vram_size = 1
        else:
            # Mario, Mallow, Geno, Peach — cloneable, use buffer system
            obj._min_vram_size = 0
        obj._cannot_clone = True


__all__ = ["MarrymoreCharacter"]
