from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3780_jmp_if_mario_in_air_0',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3780_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, RadialDirections.SOUTHEAST, 25, 114, 0, []]
    },
    {
        "identifier": 'EVENT_3780_db_2',
        "command": 'db',
        "args": [0xfd, 0x49]
    },
    {
        "identifier": 'EVENT_3780_jmp_to_subroutine_3',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3780_jmp_if_present_in_current_level_9']
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_4_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3780_action_queue_sync_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3780_action_queue_sync_4_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [132]
            },
            {
                "identifier": 'EVENT_3780_action_queue_sync_4_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3780_action_queue_sync_4_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3780_action_queue_sync_4_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3780_action_queue_sync_4_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3780_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3780_jmp_if_mario_in_air_7',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3780_pause_6']
    },
    {
        "identifier": 'EVENT_3780_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3780_jmp_if_present_in_current_level_9',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_3, 'EVENT_3780_jmp_if_present_in_current_level_11']
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_10_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [6, 254, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_jmp_if_present_in_current_level_11',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_4, 'EVENT_3780_jmp_if_present_in_current_level_13']
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_12_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [6, 254, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_jmp_if_present_in_current_level_13',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_5, 'EVENT_3780_jmp_if_present_in_current_level_15']
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_14_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [6, 254, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_jmp_if_present_in_current_level_15',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_6, 'EVENT_3780_jmp_if_present_in_current_level_17']
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_16_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [6, 254, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_jmp_if_present_in_current_level_17',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.NPC_7, 'EVENT_3780_action_queue_sync_19']
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_18_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [6, 254, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_19_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_jmp_if_object_not_in_level_20',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_0, Rooms._380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, 'EVENT_3780_ret_23']
    },
    {
        "identifier": 'EVENT_3780_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3780_action_queue_sync_21_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3780_action_queue_sync_21_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3780_remove_from_current_level_22',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_3780_ret_23',
        "command": 'ret'
    }
]
