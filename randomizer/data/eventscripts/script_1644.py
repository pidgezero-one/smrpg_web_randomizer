from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1644_set_0',
        "command": 'set',
        "args": [0x70df, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_fade_out_music_to_volume_1',
        "command": 'fade_out_music_to_volume',
        "args": [1, 127],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 4, 'EVENT_1644_enter_area_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x707a, 3, 'EVENT_1644_run_background_event_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_remove_from_current_level_6',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_remove_from_current_level_10',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_1644_jmp_if_bit_set_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_run_background_event_12',
        "command": 'run_background_event',
        "args": [1618, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x707a, 4, 'EVENT_1644_fade_in_from_black_async_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1644_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 45, 24, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1644_action_queue_async_14_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1644_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_fade_in_from_black_async_16',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_enter_area_18',
        "command": 'enter_area',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, RadialDirections.SOUTHWEST, 17, 44, 4, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_jmp_if_bit_clear_19',
        "command": 'jmp_if_bit_clear',
        "args": [0x7042, 1, 'EVENT_1644_fade_in_from_black_async_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_apply_tile_mod_20',
        "command": 'apply_tile_mod',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_fade_in_from_black_async_21',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1644_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
