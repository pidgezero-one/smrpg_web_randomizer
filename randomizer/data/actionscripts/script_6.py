from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_6_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_6_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_6_visibility_off_2',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_6_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_6_set_vram_priority_0']
    }
]
