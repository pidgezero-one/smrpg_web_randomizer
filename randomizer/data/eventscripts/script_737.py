from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_737_palette_set_0',
        "command": 'palette_set',
        "args": [110, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x705e, 4, 'EVENT_737_set_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_set_random_2',
        "command": 'set_random',
        "args": [0x7000, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_737_action_queue_async_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_737_set_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_737_action_queue_async_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_737_set_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_737_action_queue_async_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_8',
        "command": 'jmp',
        "args": ['EVENT_737_set_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_737_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_737_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_737_set_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_737_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_737_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_737_set_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_737_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_737_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_737_palette_set_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 2, 'EVENT_737_action_queue_async_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_737_action_queue_async_19_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 17, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_737_action_queue_async_19_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_737_fade_in_from_black_async_20',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_ret_21',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_palette_set_22',
        "command": 'palette_set',
        "args": [109, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_737_action_queue_sync_23_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 22, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_737_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_737_action_queue_async_24_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_737_action_queue_async_24_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_737_stop_sound_25',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_26',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_27',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_28',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_29',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_30',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_31',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_32',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_33',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_34',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_35',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_stop_sound_36',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_unsync_action_script_37',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_737_action_queue_async_38_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 22, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_737_action_queue_async_38_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [254, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_737_fade_in_from_black_async_39',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_737_ret_40',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
