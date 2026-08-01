from __future__ import annotations
from randomizer.data.items.items import (BroochItem)
from randomizer.data.physical_objects.bosses import (SPR0207_BROOCH)
from randomizer.data.physical_objects.items import (BroochObject)
from randomizer.data.variables.event_script_names import (E0215_HILL_ITEM, E3932_GET_BROOCH, E3936_FREESTANDING_BROOCH, E3940_RIVER_BROOCH, E3944_BROOCH_CHEST)
from randomizer.data.variables.variable_names import (ITEM_ID, WEDDING_GEAR_COUNTER)
from randomizer.types.prize import (FortuneEnum, KeyPrize, TreasureHunterNickname, WeddingGearPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (Inc, JmpToEvent, SetVarToConst)


class BroochPrize(WeddingGearPrize, KeyPrize):
    item = BroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch", description="It looks pretty stylish."
    )
    _model = BroochObject
    _packet_data = (SPR0207_BROOCH, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3944_BROOCH_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3932_GET_BROOCH)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3936_FREESTANDING_BROOCH)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3940_RIVER_BROOCH)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, BroochItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


__all__ = ["BroochPrize"]
