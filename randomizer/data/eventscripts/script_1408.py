from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1408_set_bit_0',
        "command": 'set_bit',
        "args": [0x7065, 1]
    },
    {
        "identifier": 'EVENT_1408_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 0, 'EVENT_1408_action_queue_sync_3']
    },
    {
        "identifier": 'EVENT_1408_apply_tile_mod_2',
        "command": 'apply_tile_mod',
        "args": [Rooms._016_MARIOS_PAD, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1408_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1408_action_queue_sync_3_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1408_action_queue_sync_3_SUBSCRIPT_ret_1',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1408_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1408_action_queue_async_4_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1408_action_queue_async_4_SUBSCRIPT_ret_1',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1408_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7052, 2, 'EVENT_1408_ret_12']
    },
    {
        "identifier": 'EVENT_1408_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 1, 'EVENT_1408_play_music_default_volume_13']
    },
    {
        "identifier": 'EVENT_1408_play_music_default_volume_7',
        "command": 'play_music_default_volume',
        "args": [Music._14_MARIOS_PAD]
    },
    {
        "identifier": 'EVENT_1408_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1408_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1408_run_event_as_subroutine_25']
    },
    {
        "identifier": 'EVENT_1408_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 0, 'EVENT_1408_reset_coords_19']
    },
    {
        "identifier": 'EVENT_1408_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1408_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1408_play_music_default_volume_13',
        "command": 'play_music_default_volume',
        "args": [Music._14_MARIOS_PAD]
    },
    {
        "identifier": 'EVENT_1408_remove_from_current_level_14',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1408_remove_from_current_level_15',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1408_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1408_run_event_as_subroutine_25']
    },
    {
        "identifier": 'EVENT_1408_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1408_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1408_reset_coords_19',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1408_pause_20',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1408_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 146]
    },
    {
        "identifier": 'EVENT_1408_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1408_run_event_as_subroutine_25']
    },
    {
        "identifier": 'EVENT_1408_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1408_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1408_run_event_as_subroutine_25',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_1408_ret_26',
        "command": 'ret'
    }
]
