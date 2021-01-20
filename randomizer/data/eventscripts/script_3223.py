from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3223_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_3223_play_sound_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3223_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 338],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x707d, 0, 'EVENT_3223_ret_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_set_short_5',
        "command": 'set_short',
        "args": [0x7010, 0x000f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_set_short_6',
        "command": 'set_short',
        "args": [0x7012, 0x0075],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_set_short_7',
        "command": 'set_short',
        "args": [0x7014, 0x000f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_db_8',
        "command": 'db',
        "args": [0xfd, 0xc4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_pause_9',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_create_packet_event_at_coords_jmp_if_null_10',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._036_MUSHROOM_JUMPS, 0x0cd8, 'EVENT_3223_pause_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._022_CLOSE_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3223_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3223_action_queue_sync_13_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3223_action_queue_sync_13_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3223_action_queue_sync_13_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3223_action_queue_sync_13_SUBSCRIPT_end_loop_3',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3223_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
