
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1767_enable_controls_until_return_6_',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1767_set_bit_0',
        "command": 'set_bit',
        "args": [0x704f, 2]
    },
    {
        "identifier": 'EVENT_1767_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7050, 6]
    },
    {
        "identifier": 'EVENT_1767_apply_solidity_mod_3',
        "command": 'apply_solidity_mod',
        "args": [Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1767_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._017_OPEN_FRONT_GATE, 6]
    },
    {
        "identifier": 'EVENT_1767_action_queue_async_5',
        "command": 'action_queue',
        'args': [AreaObjects.LAYER_1, False],
        "subscript": [
            {
                "identifier": 'EVENT_1767_action_queue_async_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_5_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_5_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1767_action_queue_async_6',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, False],
        "subscript": [
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_transfer_xyzf_steps_0',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 18, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4]]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_object_memory_set_bit_4',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_shadow_on_5',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_db_8',
                "command": 'jmp_if_object_in_air',
                "args": [AreaObjects.NPC_4, 'EVENT_1767_action_queue_async_6_SUBSCRIPT_pause_7']
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
            {
                "identifier": 'EVENT_1767_action_queue_async_6_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [55]
            }
        ]
    },
    {
        "identifier": 'EVENT_1767_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1767_action_queue_sync_7',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": 'EVENT_1767_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1767_action_queue_sync_7_SUBSCRIPT_set_700C_to_object_coord_1',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.Z, [7], CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_1767_action_queue_sync_7_SUBSCRIPT_jmp_if_700C_equals_short_2',
                "command": "jmp_if_var_equals_const",
                "args": [0x700C, 0, 'EVENT_1767_ret_8']
            },
            {
                "identifier": 'EVENT_1767_action_queue_sync_7_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1767_action_queue_sync_7_SUBSCRIPT_jmp_4',
                "command": 'jmp',
                "args": ['EVENT_1767_action_queue_sync_7_SUBSCRIPT_pause_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_1767_ret_8',
        "command": 'ret'
    }
]
