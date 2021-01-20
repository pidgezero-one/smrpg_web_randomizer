from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_433_jmp_if_mario_in_air_0',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_store_coin_amount_7000_1',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_433_action_queue_sync_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_summon_to_current_level_at_marios_coords_3',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 24, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_set_random_2',
                "command": 'set_random',
                "args": [0x700c, 8]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_face_east_3',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_shift_f_direction_pixels_6',
                "command": 'shift_f_direction_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_shift_f_direction_pixels_8',
                "command": 'shift_f_direction_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_4_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_433_summon_to_current_level_at_marios_coords_5',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_floating_off_0',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 24, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_set_random_2',
                "command": 'set_random',
                "args": [0x700c, 8]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_face_east_3',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_shift_f_direction_pixels_6',
                "command": 'shift_f_direction_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_floating_on_7',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_shift_f_direction_pixels_8',
                "command": 'shift_f_direction_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_6_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_433_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_set_8',
        "command": 'set',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_dec_coins_9',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_433_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_10_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_433_action_queue_sync_10_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_433_pause_11',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_jmp_if_object_in_air_12',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.MEM_70A8, 'EVENT_433_pause_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_433_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
