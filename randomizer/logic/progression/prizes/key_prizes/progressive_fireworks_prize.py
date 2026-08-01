from __future__ import annotations
from randomizer.data.items.items import (FireworksItem)
from randomizer.data.physical_objects.items import (ProgressiveFireworksObject)
from randomizer.data.variables.event_script_names import (E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS, E0217_HILL_FIREWORKS, E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT, E3113_FREESTANDING_PROGRESSIVE_FIREWORKS_GRANT, E3399_MIDAS_CAVE_PROGRESSIVE_FIREWORK_GRANTER)
from randomizer.types.prize import (FortuneEnum, KeyPrize, ProgressiveItemPrize, TreasureHunterNickname)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class ProgressiveFireworksPrize(ProgressiveItemPrize, KeyPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = ProgressiveFireworksObject
    _fortune_type: FortuneEnum = FortuneEnum.RARE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3113_FREESTANDING_PROGRESSIVE_FIREWORKS_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3399_MIDAS_CAVE_PROGRESSIVE_FIREWORK_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0217_HILL_FIREWORKS)])


__all__ = ["ProgressiveFireworksPrize"]
