from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3790_jmp_if_mario_in_air_0',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, RadialDirections.NORTHWEST, 16, 84, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_db_2',
        "command": 'db',
        "args": [0xfd, 0x49],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_jmp_to_subroutine_3',
        "command": 'jmp_to_subroutine',
        "args": [0xc3da],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3790_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3790_action_queue_sync_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3790_action_queue_sync_4_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [132]
            },
            {
                "identifier": 'EVENT_3790_action_queue_sync_4_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3790_action_queue_sync_4_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3790_action_queue_sync_4_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3790_action_queue_sync_4_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3790_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_pause_6',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_jmp_if_mario_in_air_7',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3790_pause_6'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_jmp_if_present_in_current_level_9',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_3790_jmp_if_present_in_current_level_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3790_action_queue_sync_10_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3790_jmp_if_present_in_current_level_11',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_4, 'EVENT_3790_jmp_if_present_in_current_level_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3790_action_queue_sync_12_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3790_jmp_if_present_in_current_level_13',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_5, 'EVENT_3790_jmp_if_present_in_current_level_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3790_action_queue_sync_14_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3790_jmp_if_present_in_current_level_15',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_6, 'EVENT_3790_jmp_if_present_in_current_level_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3790_action_queue_sync_16_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3790_jmp_if_present_in_current_level_17',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_7, 'EVENT_3790_remember_last_object_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3790_action_queue_sync_18_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3790_remember_last_object_19',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3790_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
