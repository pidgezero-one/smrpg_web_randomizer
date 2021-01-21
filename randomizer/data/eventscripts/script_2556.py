from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2556_start_battle_0',
        "command": 'start_battle',
        "args": [0x00ad, 41]
    },
    {
        "identifier": 'EVENT_2556_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2556_restore_all_hp_3']
    },
    {
        "identifier": 'EVENT_2556_reset_and_choose_game_2',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2556_restore_all_hp_3',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2556_restore_all_fp_4',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2556_set_bit_5',
        "command": 'set_bit',
        "args": [0x708c, 3]
    },
    {
        "identifier": 'EVENT_2556_remove_from_level_6',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._254_BEAN_VALLEY_SMILAX_AREA]
    },
    {
        "identifier": 'EVENT_2556_remove_from_level_7',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._254_BEAN_VALLEY_SMILAX_AREA]
    },
    {
        "identifier": 'EVENT_2556_remove_from_level_8',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._254_BEAN_VALLEY_SMILAX_AREA]
    },
    {
        "identifier": 'EVENT_2556_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._254_BEAN_VALLEY_SMILAX_AREA]
    },
    {
        "identifier": 'EVENT_2556_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2556_remove_from_current_level_11',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2556_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2556_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2556_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2556_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2556_action_queue_async_14_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2556_pause_15',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2556_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2556_action_queue_sync_16_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2556_action_queue_sync_16_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2556_action_queue_sync_16_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2556_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2556_action_queue_sync_16_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2556_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2556_pause_17',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_2556_pause_18',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2556_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2556_action_queue_sync_19_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2556_action_queue_sync_19_SUBSCRIPT_shadow_on_1',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_2556_action_queue_sync_19_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2556_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 689]
    },
    {
        "identifier": 'EVENT_2556_set_short_21',
        "command": 'set_short',
        "args": [0x700a, 0x00da]
    },
    {
        "identifier": 'EVENT_2556_jmp_to_event_22',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_2556_stop_sound_23',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2556_stop_sound_24',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2556_stop_sound_25',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2556_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2556_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_2556_ret_28',
        "command": 'ret'
    }
]
