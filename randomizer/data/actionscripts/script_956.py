from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_956_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_956_pause_1',
        "command": 'pause',
        "args": [56]
    },
    {
        "identifier": 'ACTION_956_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_953_set_animation_speed_0']
    }
]
