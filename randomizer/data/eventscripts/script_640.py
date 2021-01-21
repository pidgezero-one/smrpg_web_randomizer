from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_640_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_640_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_640_action_queue_async_6']
    },
    {
        "identifier": 'EVENT_640_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 5, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_640_set_bit_3',
        "command": 'set_bit',
        "args": [0x704c, 5]
    },
    {
        "identifier": 'EVENT_640_pause_4',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_640_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_640_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_5_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_5_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [20, 17]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_5_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_640_action_queue_async_5_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_5_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_640_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [20, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_6_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_640_jmp_7',
        "command": 'jmp',
        "args": ['EVENT_640_action_queue_async_14']
    },
    {
        "identifier": 'EVENT_640_pause_8',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_640_run_dialog_9',
        "command": 'run_dialog',
        "args": [2074, AreaObjects.NPC_3, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_640_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_640_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_640_pause_11',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_640_run_dialog_12',
        "command": 'run_dialog',
        "args": [2075, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_640_pause_13',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_640_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_640_action_queue_async_14_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_640_action_queue_async_14_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [18, 19]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_14_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_640_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 31]
    },
    {
        "identifier": 'EVENT_640_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_640_action_queue_async_16_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_640_action_queue_async_16_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_640_ret_17',
        "command": 'ret'
    }
]
