# pylint: disable=C0301

"""E1677_TEMPLE_PIPE_TO_MONSTRO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN, ["EVENT_1677_ret"]
        ),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RemoveObjectFromSpecificLevel(NPC_1, R317_LANDS_END_DESERT_AREA_01),
        RemoveObjectFromSpecificLevel(NPC_0, R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS),
        RemoveObjectFromSpecificLevel(
            NPC_0, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
        ),
        SetBit(MOUSE_RETURNED_TO_MONSTRO),
        SetVarToConst(X_COORD_2, 7470),
        RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
        SetBit(MAP_MONSTRO_TOWN),
        SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
        EnterArea(
            room_id=R324_MONSTRO_TOWN_OUTSIDE,
            face_direction=SOUTH,
            x=2,
            y=47,
            z=16,
            show_banner=True,
        ),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        JmpToEvent(E2048_MONSTRO_TOWN_EXTERIOR_LOADER),
        Return(identifier="EVENT_1677_ret"),
    ]
)
