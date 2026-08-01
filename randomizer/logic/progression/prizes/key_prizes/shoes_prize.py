from __future__ import annotations
from randomizer.data.items.items import (ShoesItem)
from randomizer.data.physical_objects.bosses import (SPR0202_SHOES)
from randomizer.data.physical_objects.items import (ShoesObject)
from randomizer.data.variables.event_script_names import (E0215_HILL_ITEM, E3931_GET_SHOES, E3935_FREESTANDING_SHOES, E3939_RIVER_SHOES, E3943_SHOES_CHEST)
from randomizer.data.variables.variable_names import (ITEM_ID, WEDDING_GEAR_COUNTER)
from randomizer.types.prize import (FortuneEnum, KeyPrize, TreasureHunterNickname, WeddingGearPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (Inc, JmpToEvent, SetVarToConst)


class ShoesPrize(WeddingGearPrize, KeyPrize):
    item = ShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Ruby Slippers", description="Do you think they'll take you\n home?"
    )
    _model = ShoesObject
    _packet_data = (SPR0202_SHOES, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3943_SHOES_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3931_GET_SHOES)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3935_FREESTANDING_SHOES)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3939_RIVER_SHOES)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, ShoesItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


__all__ = ["ShoesPrize"]
