from __future__ import annotations
from randomizer.data.physical_objects.bosses import (SPR0237_EGG)
from randomizer.data.physical_objects.items import (EggObject)
from randomizer.data.variables.event_script_names import (E3087_PROGRESSIVE_EGG_UPGRADE, E3098_PROGRESSIVE_EGG_NPC_GRANT, E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT, E3114_HILL_PROGRESSIVE_EGG, E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER)
from randomizer.types.prize import (ProgressiveItemPrize, TreasureHunterNickname)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class ProgressiveEggPrize(ProgressiveItemPrize):
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?",
    )
    _model = EggObject
    _packet_data = (SPR0237_EGG, 0)

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3087_PROGRESSIVE_EGG_UPGRADE)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3098_PROGRESSIVE_EGG_NPC_GRANT)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3114_HILL_PROGRESSIVE_EGG)])


__all__ = ["ProgressiveEggPrize"]
