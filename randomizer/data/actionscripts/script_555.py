from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_555_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_555_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_555_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_555_db_3',
        "command": 'db',
        "args": [0xfd, 0x12]
    },
    {
        "identifier": 'ACTION_555_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_555_db_5',
        "command": 'db',
        "args": [0xc8, 0x98]
    },
    {
        "identifier": 'ACTION_555_db_6',
        "command": 'db',
        "args": [0x9a]
    },
    {
        "identifier": 'ACTION_555_set_vram_priority_7',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_555_visibility_on_8',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_555_object_memory_clear_bit_9',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_555_jump_to_height_10',
        "command": 'jump_to_height',
        "args": [48]
    },
    {
        "identifier": 'ACTION_555_walk_1_step_northwest_11',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_555_set_vram_priority_12',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_555_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_555_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_555_pause_15',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'ACTION_555_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_555_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_404_face_mario_3']
    }
]
