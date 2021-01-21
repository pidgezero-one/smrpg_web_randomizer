from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_398_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_398_run_dialog_11']
    },
    {
        "identifier": 'EVENT_398_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_398_jmp_if_bit_set_13']
    },
    {
        "identifier": 'EVENT_398_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7084, 4, 'EVENT_398_jmp_if_bit_set_5']
    },
    {
        "identifier": 'EVENT_398_run_dialog_3',
        "command": 'run_dialog',
        "args": [688, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_398_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 1, 'EVENT_398_run_dialog_11']
    },
    {
        "identifier": 'EVENT_398_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_398_run_dialog_9']
    },
    {
        "identifier": 'EVENT_398_run_dialog_7',
        "command": 'run_dialog',
        "args": [722, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_398_run_dialog_9',
        "command": 'run_dialog',
        "args": [723, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_398_run_dialog_11',
        "command": 'run_dialog',
        "args": [731, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_398_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x705d, 7, 'EVENT_398_run_dialog_32']
    },
    {
        "identifier": 'EVENT_398_set_bit_14',
        "command": 'set_bit',
        "args": [0x705d, 7]
    },
    {
        "identifier": 'EVENT_398_run_dialog_15',
        "command": 'run_dialog',
        "args": [688, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_398_action_queue_async_16_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_16_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [3, 65]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_16_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_398_action_queue_async_16_SUBSCRIPT_face_north_3',
                "command": 'face_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_398_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_398_action_queue_async_17_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_398_action_queue_async_17_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 66, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_17_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_17_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_398_action_queue_async_17_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_17_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_398_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_398_action_queue_async_18_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_398_run_dialog_19',
        "command": 'run_dialog',
        "args": [2323, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_398_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_20_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_398_pause_21',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_398_run_dialog_22',
        "command": 'run_dialog',
        "args": [2324, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_run_dialog_23',
        "command": 'run_dialog',
        "args": [2325, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_pause_24',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_398_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_398_action_queue_async_25_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_25_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_25_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_398_pause_26',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_398_run_dialog_27',
        "command": 'run_dialog',
        "args": [2326, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_pause_28',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_398_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_398_action_queue_sync_29_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_398_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_398_action_queue_async_30_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_398_action_queue_async_30_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [16, 66, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_398_ret_31',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_398_run_dialog_32',
        "command": 'run_dialog',
        "args": [2327, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_398_ret_33',
        "command": 'ret'
    }
]
