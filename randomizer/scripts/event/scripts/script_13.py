# E0013_BASE_ROM_ONLY_FIX_MAP_AND_PARTY

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
        CharacterJoinsParty(MARIO),
        CharacterLeavesParty(DUMMY_0X05),
        JmpToEvent(E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS),
    ]
)
