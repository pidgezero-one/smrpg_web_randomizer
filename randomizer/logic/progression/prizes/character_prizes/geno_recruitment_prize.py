from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.allies.allies import (GENO_Ally)
from randomizer.data.physical_objects.characters import (GenoCharacterNPC)
from randomizer.data.variables.dialog_names import (DI1181_GENO_JOINS)
from randomizer.data.variables.variable_names import (MOLEVILLE_MINES_ENTRANCE_GATING, PIPE_VAULT_GATED, TOWER_CHARACTER_RECRUITED)
from randomizer.types.prize import (CharacterName, CharacterPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (BOWSER, GENO)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (CharacterJoinsParty, ClearBit, Return, RunDialog, SetBit)
from randomizer.types.flags import (BoosterTowerGate, BoosterTowerGating, Moleville1Gate, Moleville1Gating, PipeVaultGate, PipeVaultGating)

if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class GenoRecruitmentPrize(CharacterPrize):
    _ally = GENO_Ally
    _name_props = CharacterName(
        "`GENO_NAME`", "man", "guy", "sir", "mister", "Mr", "mate", ", man", "puppet"
    )
    _character_model = GenoCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(GENO)]
        if world.settings.is_flag_value(
            PipeVaultGate, PipeVaultGating.GENO
        ):
            output.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        if world.settings.is_flag_value(
            Moleville1Gate, Moleville1Gating.GENO
        ):
            output.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1181_GENO_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            BoosterTowerGate, BoosterTowerGating.GENO
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


__all__ = ["GenoRecruitmentPrize"]
