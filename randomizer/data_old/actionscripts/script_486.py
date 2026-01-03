
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_486_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_486_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_486_ret_3',
        "command": 'ret'
    }
]
