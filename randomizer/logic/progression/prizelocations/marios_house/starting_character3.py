from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StartingCharacterLocation, WorldAreaEnum)


class StartingCharacter3(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_3
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1222_STARTING_CHARACTER_3
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


__all__ = ["StartingCharacter3"]
