from __future__ import annotations
from randomizer.data.items.items import (RingItem)
from randomizer.data.physical_objects.bosses import (SPR0196_RING)
from randomizer.data.physical_objects.items import (RingObject)
from randomizer.data.variables.event_script_names import (E0215_HILL_ITEM, E3933_GET_RING, E3937_FREESTANDING_RING, E3941_RIVER_RING, E3945_RING_CHEST)
from randomizer.data.variables.variable_names import (ITEM_ID, WEDDING_GEAR_COUNTER)
from randomizer.types.prize import (FortuneEnum, KeyPrize, TreasureHunterNickname, WeddingGearPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (Inc, JmpToEvent, SetVarToConst)


class RingPrize(WeddingGearPrize, KeyPrize):
    item = RingItem
    _nickname = TreasureHunterNickname(
        nickname="Wedding Ring", description="For that special someone!"
    )
    _model = RingObject
    _packet_data = (SPR0196_RING, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3945_RING_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3933_GET_RING)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3937_FREESTANDING_RING)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3941_RIVER_RING)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, RingItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


__all__ = ["RingPrize"]
