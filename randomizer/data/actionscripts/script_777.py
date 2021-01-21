from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_777_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_777_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_777_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_777_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_777_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_777_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_777_add_z_coord_1_step_6',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_777_pause_7',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_777_visibility_off_8',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_777_db_9',
        "command": 'db',
        "args": [0xfd, 0xf2]
    },
    {
        "identifier": 'ACTION_777_ret_10',
        "command": 'ret'
    }
]
