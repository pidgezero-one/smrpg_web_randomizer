from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_clear_mines, is_all_starting_chars_set, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (AllyNPCSub, CharacterRecruitmentLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_WalkEastPixels, A_WalkNorthPixels)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerMinesCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = BowserRecruitmentPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_CHARACTER
    _world_area = WorldAreaEnum.MOLEVILLE
    _container_event = E1227_MOLEVILLE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
            NPC_1,
        ),
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 128),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(MINES_BACK_OPENED, ["next"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(8)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        # starters need to be set first
        return can_clear_mines(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )
    
    def render(self, world: GameWorld):
        op = super().render(world)
        if isinstance(self.prize, MarioRecruitmentPrize):
            world.event_scripts.get_subscript_command_by_identifier(
                "mines_character_reposition", "mines_character_reposition_y", A_WalkNorthPixels
            ).set_pixels(10)
            world.event_scripts.get_subscript_command_by_identifier(
                "mines_character_reposition", "mines_character_reposition_x", A_WalkEastPixels
            ).set_pixels(7)
        elif isinstance(self.prize, (GenoRecruitmentPrize, ToadstoolRecruitmentPrize)):
            world.event_scripts.get_subscript_command_by_identifier(
                "mines_character_reposition", "mines_character_reposition_y", A_WalkNorthPixels
            ).set_pixels(5)
            world.event_scripts.get_subscript_command_by_identifier(
                "mines_character_reposition", "mines_character_reposition_x", A_WalkEastPixels
            ).set_pixels(6)
        elif isinstance(self.prize, MallowRecruitmentPrize):
            world.event_scripts.get_subscript_command_by_identifier(
                "mines_character_reposition", "mines_character_reposition_y", A_WalkNorthPixels
            ).set_pixels(6)
            world.event_scripts.get_subscript_command_by_identifier(
                "mines_character_reposition", "mines_character_reposition_x", A_WalkEastPixels
            ).set_pixels(7)
        elif self.prize is None:
            pass
        else:
            world.event_scripts.delete_subscript_command_by_identifier("mines_character_reposition", "mines_character_reposition_y")
            world.event_scripts.delete_subscript_command_by_identifier("mines_character_reposition", "mines_character_reposition_x")
        return op


__all__ = ["InnerMinesCharacter"]
