from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_952_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_952_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_952_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_952_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._145_BLACKSMITH_HAMMER_STRIKE, 4]
    },
    {
        "identifier": 'ACTION_952_pause_4',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_952_ret_5',
        "command": 'ret'
    }
]
