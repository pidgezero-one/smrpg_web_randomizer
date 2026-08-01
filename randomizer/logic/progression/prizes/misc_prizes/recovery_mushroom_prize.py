from __future__ import annotations
from randomizer.data.physical_objects.bosses import (SPR0195_FLOWER)
from randomizer.data.physical_objects.items import (RecoveryMushroomObject)
from randomizer.data.variables.event_script_names import (E0397_HEAL_IN_TOADSTOOLS_ROOM, E2822_ASYNC_NO_ANIMATION_MUSHROOM, E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, E4091_ASYNC_NO_ANIMATION_MUSHROOM_PACKET)
from randomizer.data.variables.variable_names import (ITEM_ID)
from randomizer.types.prize import (FortuneEnum, StandardPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent, SetVarToConst)


class RecoveryMushroomPrize(StandardPrize):
    _model = RecoveryMushroomObject
    _packet_data = (SPR0195_FLOWER, 1)
    _fortune_type: FortuneEnum = FortuneEnum.MEAL

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 0),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0397_HEAL_IN_TOADSTOOLS_ROOM)])

    @property
    def standing_grant(self) -> EventScript:
        # No action queue in front of the jump: a sync queue blocks the main event thread
        # for a couple of frames (player input locked) and E2822's
        # RemoveObjectFromCurrentLevel already despawns the NPC in-frame.
        return EventScript([JmpToEvent(E2822_ASYNC_NO_ANIMATION_MUSHROOM)])

    @property
    def packet_grant(self) -> EventScript:
        # E4091 already does the object-local hide + heal, so just jump straight to it.
        return EventScript([JmpToEvent(E4091_ASYNC_NO_ANIMATION_MUSHROOM_PACKET)])


__all__ = ["RecoveryMushroomPrize"]
