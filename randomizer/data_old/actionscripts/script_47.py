
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_47_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_47_db_1',
        "command": 'db',
        "args": [0xc8, 0x23]
    },
    {
        "identifier": 'ACTION_47_add_short_2',
        "command": "add_const_to_var",
        "args": [0x7016, 0x00e0]
    },
    {
        "identifier": 'ACTION_47_add_short_3',
        "command": "add_const_to_var",
        "args": [0x7018, 0x0070]
    },
    {
        "identifier": 'ACTION_47_add_short_4',
        "command": "add_const_to_var",
        "args": [0x701a, 0x0180]
    },
    {
        "identifier": 'ACTION_47_db_5',
        "command": 'transfer_to_7016_7018_701A'
    },
    {
        "identifier": 'ACTION_47_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._113_OPEN_CHAMBER_DOOR, 4]
    },
    {
        "identifier": 'ACTION_47_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_47_set_short_8',
        "command": "set_var_to_const",
        "args": [0x7034, 0xffff]
    },
    {
        "identifier": 'ACTION_47_create_packet_at_npc_coords_9',
        "command": 'create_packet_at_npc_coords',
        "args": [NPCPackets._032_BLUE_CLOUD, AreaObjects.DUMMY_0X07, 'ACTION_47_set_animation_speed_10']
    },
    {
        "identifier": 'ACTION_47_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_47_set_bit_11',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_47_shift_southeast_steps_12',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_47_set_vram_priority_13',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_47_shift_southeast_steps_14',
        "command": 'shift_southeast_steps',
        "args": [15]
    },
    {
        "identifier": 'ACTION_47_set_vram_priority_15',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_47_shift_southeast_steps_16',
        "command": 'shift_southeast_steps',
        "args": [12]
    },
    {
        "identifier": 'ACTION_47_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_47_ret_18',
        "command": 'ret'
    }
]
