from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1308_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_1308_ret_11']
    },
    {
        "identifier": 'EVENT_1308_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1308_create_packet_at_object_coords_jmp_if_null_2',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._034_GREY_EXPLOSION_SFX, AreaObjects.MARIO, 'EVENT_1308_jmp_if_bit_set_0']
    },
    {
        "identifier": 'EVENT_1308_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [27, 29, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_shift_north_steps_11',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1308_action_queue_sync_3_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1308_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1308_action_queue_async_4_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1308_action_queue_async_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_1308_start_battle_5',
        "command": 'start_battle',
        "args": [0x008f, 12]
    },
    {
        "identifier": 'EVENT_1308_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_1308_set_bit_8']
    },
    {
        "identifier": 'EVENT_1308_reset_and_choose_game_7',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1308_set_bit_8',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1308_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1308_action_queue_sync_9_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1308_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1308_ret_11',
        "command": 'ret'
    }
]
