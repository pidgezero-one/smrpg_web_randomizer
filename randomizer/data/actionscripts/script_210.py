from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_210_jump_to_height_silent_0',
        "command": 'jump_to_height_silent',
        "args": [96]
    },
    {
        "identifier": 'ACTION_210_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_210_pause_2',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_210_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_210_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_210_jmp_if_mario_in_air_5',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_210_pause_4']
    },
    {
        "identifier": 'ACTION_210_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_210_ret_7',
        "command": 'ret'
    }
]
