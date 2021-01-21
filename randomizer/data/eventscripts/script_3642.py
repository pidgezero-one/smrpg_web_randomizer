from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3642_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 3, 'EVENT_3642_jmp_if_bit_clear_2']
    },
    {
        "identifier": 'EVENT_3642_apply_solidity_mod_1',
        "command": 'apply_solidity_mod',
        "args": [Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3642_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x705f, 5, 'EVENT_3642_set_temp_action_script_async_5']
    },
    {
        "identifier": 'EVENT_3642_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3642_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x704c, 1]
    },
    {
        "identifier": 'EVENT_3642_set_temp_action_script_async_5',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_5, 804]
    },
    {
        "identifier": 'EVENT_3642_set_temp_action_script_async_6',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_6, 807]
    },
    {
        "identifier": 'EVENT_3642_set_temp_action_script_async_7',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_1, 806]
    },
    {
        "identifier": 'EVENT_3642_set_temp_action_script_async_8',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_3, 803]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_9_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_10_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_11_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_12_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_13_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_14_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_15_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_16_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_17_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_sync_18_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_async_19_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3642_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 0, 'EVENT_3642_fade_in_from_black_sync_24']
    },
    {
        "identifier": 'EVENT_3642_fade_in_from_black_async_22',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3642_ret_23',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3642_fade_in_from_black_sync_24',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3642_action_queue_async_25',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3642_action_queue_async_25_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3642_action_queue_async_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3642_action_queue_async_25_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [132]
            },
            {
                "identifier": 'EVENT_3642_action_queue_async_25_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3642_action_queue_async_25_SUBSCRIPT_floating_on_4',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3642_action_queue_async_25_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3642_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3642_pause_script_until_effect_done_27',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3642_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_3642_ret_29',
        "command": 'ret'
    }
]
