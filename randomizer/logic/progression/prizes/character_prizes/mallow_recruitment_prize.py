from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.allies.allies import (MALLOW_Ally)
from randomizer.data.physical_objects.characters import (MallowCharacterNPC)
from randomizer.data.variables.dialog_names import (DI1180_MALLOW_JOINS)
from randomizer.data.variables.room_names import (R333_KERO_SEWERS_ENTRANCE)
from randomizer.data.variables.variable_names import (MAP_BANDITS_WAY, MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY, SEWERS_CLOSED, TOWER_CHARACTER_RECRUITED)
from randomizer.types.prize import (CharacterName, CharacterPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import (NPC_1)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (BOWSER, MALLOW, NPC_0)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (CharacterJoinsParty, ClearBit, RemoveObjectFromSpecificLevel, Return, RunDialog, SetBit)
from randomizer.types.flags import (BanditsWayGate, BanditsWayGating, BoosterTowerGate, BoosterTowerGating, KeroSewersGate, KeroSewersGating)

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (UsableEventScriptCommand)
    from randomizer.types.gameworld import (GameWorld)


class MallowRecruitmentPrize(CharacterPrize):
    _ally = MALLOW_Ally
    _name_props = CharacterName(
        "`MALLOW_NAME`", "boy", "guy", "sir", "mister", "Mr", "kid", ", kid", "puffball"
    )
    _character_model = MallowCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(MALLOW)]
        if world.settings.is_flag_value(
            BanditsWayGate, BanditsWayGating.MALLOW
        ):
            output.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        if world.settings.is_flag_value(
            KeroSewersGate, KeroSewersGating.MALLOW
        ):
            output.extend(
                [
                    ClearBit(SEWERS_CLOSED),
                    RemoveObjectFromSpecificLevel(NPC_0, R333_KERO_SEWERS_ENTRANCE),
                    RemoveObjectFromSpecificLevel(NPC_1, R333_KERO_SEWERS_ENTRANCE),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1180_MALLOW_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            BoosterTowerGate, BoosterTowerGating.MALLOW
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


__all__ = ["MallowRecruitmentPrize"]
