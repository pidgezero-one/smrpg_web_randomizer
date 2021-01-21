from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_106_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_106_db_1',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_106_db_2',
        "command": 'db',
        "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_106_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._033_JUMPING_BOUNCING_FISH, 6]
    },
    {
        "identifier": 'ACTION_106_walk_1_step_northeast_4',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_106_shift_northeast_pixels_5',
        "command": 'shift_northeast_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_106_bpl_26_27_28_6',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_106_pause_7',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_106_ret_8',
        "command": 'ret'
    }
]
