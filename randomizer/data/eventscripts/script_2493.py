from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2493_set_short_0',
        "command": 'set_short',
        "args": [0x700a, 0x00e1]
    },
    {
        "identifier": 'EVENT_2493_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [720]
    },
    {
        "identifier": 'EVENT_2493_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._005_BLOCK_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_2493_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2493_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_3_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2493_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_bpl_26_27_28_7',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2493_set_7010_to_object_xyz_5',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2493_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_2493_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_2493_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7064, 6]
    },
    {
        "identifier": 'EVENT_2493_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2493_create_packet_at_7010_coords_jmp_if_null_10',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._004_MONSTER_FACE, 'EVENT_2493_pause_11']
    },
    {
        "identifier": 'EVENT_2493_pause_11',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2493_stop_embedded_action_script_12',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2493_start_battle_13',
        "command": 'start_battle',
        "args": [0x009e, 21]
    },
    {
        "identifier": 'EVENT_2493_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_2493_reset_and_choose_game_25']
    },
    {
        "identifier": 'EVENT_2493_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2493_action_queue_sync_15_SUBSCRIPT_shift_south_steps_0',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2493_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2493_set_bit_17',
        "command": 'set_bit',
        "args": [0x7064, 6]
    },
    {
        "identifier": 'EVENT_2493_set_bit_18',
        "command": 'set_bit',
        "args": [0x7064, 5]
    },
    {
        "identifier": 'EVENT_2493_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2493_action_queue_sync_19_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_19_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x25, 0x40, 0x00, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_19_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_19_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_19_SUBSCRIPT_object_memory_set_bit_5',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_2493_action_queue_sync_19_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2493_remove_from_level_20',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    },
    {
        "identifier": 'EVENT_2493_summon_to_level_21',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    },
    {
        "identifier": 'EVENT_2493_stop_embedded_action_script_22',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2493_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_5, 15]
    },
    {
        "identifier": 'EVENT_2493_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2493_reset_and_choose_game_25',
        "command": 'reset_and_choose_game'
    }
]
