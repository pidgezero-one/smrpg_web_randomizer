from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_720_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_720_play_sound_1',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_720_pause_2',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_720_set_3',
        "command": 'set',
        "args": [0x70af, 0]
    },
    {
        "identifier": 'ACTION_720_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_720_ret_5',
        "command": 'ret'
    }
]
