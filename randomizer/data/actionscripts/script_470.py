from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_470_db_0',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_470_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_470_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 4]
    },
    {
        "identifier": 'ACTION_470_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_470_set_priority_4',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_470_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_470_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_470_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_470_add_z_coord_1_step_8',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_470_pause_9',
        "command": 'pause',
        "args": [26]
    },
    {
        "identifier": 'ACTION_470_visibility_off_10',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_470_ret_11',
        "command": 'ret'
    }
]
