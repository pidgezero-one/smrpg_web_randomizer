from __future__ import annotations
from randomizer.data.physical_objects.bosses import (SPR0206_CARD)
from randomizer.data.physical_objects.items import (CardObject)
from randomizer.data.variables.event_script_names import (E3086_JUICE_BAR_CARD_UPGRADE, E3097_JUICE_BAR_CARD_NPC_GRANT, E3110_FREESTANDING_JUICE_BAR_CARD_GRANT, E3115_HILL_PROGRESSIVE_CARD, E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER)
from randomizer.types.prize import (FortuneEnum, KeyPrize, ProgressiveItemPrize, TreasureHunterNickname)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class ProgressiveCardPrize(ProgressiveItemPrize, KeyPrize):
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige.",
    )
    _model = CardObject
    _packet_data = (SPR0206_CARD, 0)
    _fortune_type: FortuneEnum = FortuneEnum.RARE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3086_JUICE_BAR_CARD_UPGRADE)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3097_JUICE_BAR_CARD_NPC_GRANT)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3110_FREESTANDING_JUICE_BAR_CARD_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3115_HILL_PROGRESSIVE_CARD)])


__all__ = ["ProgressiveCardPrize"]
