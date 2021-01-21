from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2497_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2497_ret_14']
    },
    {
        "identifier": 'EVENT_2497_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2497_freeze_all_npcs_until_return_2',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_2497_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._101_TERRAPIN_ATTACK, 4]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_3_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_2497_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2497_action_queue_sync_4_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_2497_pause_5',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'EVENT_2497_stop_embedded_action_script_6',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2497_start_battle_7',
        "command": 'start_battle',
        "args": [0x0001, 7]
    },
    {
        "identifier": 'EVENT_2497_jmp_if_bit_clear_8',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2497_remove_from_current_level_10']
    },
    {
        "identifier": 'EVENT_2497_reset_game_9',
        "command": 'reset_game'
    },
    {
        "identifier": 'EVENT_2497_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2497_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2497_unfreeze_all_npcs_12',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_2497_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2497_ret_14',
        "command": 'ret'
    }
]
