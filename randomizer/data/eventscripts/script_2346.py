from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2346_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2346_action_queue_sync_0_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2346_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 738]
    },
    {
        "identifier": 'EVENT_2346_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2346_action_queue_async_2_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._073_THWOMP_STOMP, 4]
            },
            {
                "identifier": 'EVENT_2346_action_queue_async_2_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_2346_action_queue_async_2_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            }
        ]
    },
    {
        "identifier": 'EVENT_2346_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2346_action_queue_sync_3_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2346_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2346_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 739]
    },
    {
        "identifier": 'EVENT_2346_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_2346_clear_bit_9']
    },
    {
        "identifier": 'EVENT_2346_set_7000_to_object_coord_7',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2346_jmp_if_7000_equals_short_8',
        "command": 'jmp_if_7000_equals_short',
        "args": [23, 'EVENT_2346_enable_controls_11']
    },
    {
        "identifier": 'EVENT_2346_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2346_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2346_enable_controls_11',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2346_freeze_camera_12',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2346_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2346_action_queue_sync_13_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [384]
            }
        ]
    },
    {
        "identifier": 'EVENT_2346_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2346_action_queue_sync_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2346_action_queue_sync_14_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2346_pause_15',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2346_fade_out_to_black_async_duration_16',
        "command": 'fade_out_to_black_async_duration',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2346_set_bit_17',
        "command": 'set_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2346_enter_area_18',
        "command": 'enter_area',
        "args": [Rooms._035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS, RadialDirections.SOUTHEAST, 3, 53, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2346_ret_19',
        "command": 'ret'
    }
]
