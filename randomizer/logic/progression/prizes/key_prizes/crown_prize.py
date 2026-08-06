from __future__ import annotations
from randomizer.data.items.items import (CrownItem)
from randomizer.data.physical_objects.bosses import (SPR0216_CROWN)
from randomizer.data.physical_objects.items import (CrownObject)
from randomizer.data.variables.event_script_names import (E0215_HILL_ITEM, E3934_GET_CROWN, E3938_FREESTANDING_CROWN, E3942_RIVER_CROWN, E3946_CROWN_CHEST)
from randomizer.data.variables.variable_names import (ITEM_ID, WEDDING_GEAR_COUNTER)
from randomizer.types.prize import (FortuneEnum, KeyPrize, TreasureHunterNickname, WeddingGearPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (Inc, JmpToEvent, SetVarToConst)


class CrownPrize(WeddingGearPrize, KeyPrize):
    item = CrownItem
    _nickname = TreasureHunterNickname(
        nickname="Gold Crown", description="It looks pretty important!"
    )
    _model = CrownObject
    _packet_data = (SPR0216_CROWN, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3946_CROWN_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3934_GET_CROWN)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3938_FREESTANDING_CROWN)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3942_RIVER_CROWN)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, CrownItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


__all__ = ["CrownPrize"]
