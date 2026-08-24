from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.allies.allies import (TOADSTOOL_Ally)
from randomizer.data.physical_objects.characters import (ToadstoolCharacterNPC)
from randomizer.data.variables.dialog_names import (DI1183_TOADSTOOL_JOINS)
from randomizer.data.variables.variable_names import (MAP_DIRECTIONAL_SEASIDE_DOWN_SEA, MAP_SEA, TOWER_CHARACTER_RECRUITED)
from randomizer.types.prize import (CharacterName, CharacterPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (BOWSER, TOADSTOOL)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (CharacterJoinsParty, Return, RunDialog, SetBit)
from randomizer.types.flags import (BoosterTowerGate, BoosterTowerGating, SeaGate, SeaGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)


class ToadstoolRecruitmentPrize(CharacterPrize):
    _ally = TOADSTOOL_Ally
    _name_props = CharacterName(
        "`PEACH_NAME`", "woman", "gal", "ma'am", "miss", "Ms", "lass", "", "lady"
    )
    _character_model = ToadstoolCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(TOADSTOOL)]
        if world.settings.is_flag_value(SeaGate, SeaGating.TOADSTOOL):
            output.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1183_TOADSTOOL_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            BoosterTowerGate, BoosterTowerGating.TOADSTOOL
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


__all__ = ["ToadstoolRecruitmentPrize"]
