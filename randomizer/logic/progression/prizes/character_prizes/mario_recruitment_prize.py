from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.allies.allies import (MARIO_Ally)
from randomizer.data.physical_objects.characters import (MarioCharacterNPC)
from randomizer.data.variables.dialog_names import (DI1179_MARIO_JOINS)
from randomizer.data.variables.variable_names import (TOWER_CHARACTER_RECRUITED)
from randomizer.types.prize import (CharacterName, CharacterPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (BOWSER, MARIO)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (CharacterJoinsParty, Return, RunDialog, SetBit)
from randomizer.types.flags import (BoosterTowerGate, BoosterTowerGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarioRecruitmentPrize(CharacterPrize):
    _ally = MARIO_Ally
    _name_props = CharacterName(
        "`MARIO_NAME`", "man", "guy", "sir", "mister", "Mr", "mate", ", man", "mustache"
    )
    _character_model = MarioCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(MARIO)]
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1179_MARIO_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            BoosterTowerGate, BoosterTowerGating.MARIO
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


__all__ = ["MarioRecruitmentPrize"]
