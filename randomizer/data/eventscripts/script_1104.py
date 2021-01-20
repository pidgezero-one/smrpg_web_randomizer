from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1104_set_bit_0',
        "command": 'set_bit',
        "args": [0x7065, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_1104_action_queue_async_1_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1104_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 1, 'EVENT_1104_deactivate_sound_channels_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 0, 'EVENT_1104_deactivate_sound_channels_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 3, 'EVENT_1104_play_music_default_volume_8'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_deactivate_sound_channels_5',
        "command": 'deactivate_sound_channels',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_ret_7',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_play_music_default_volume_8',
        "command": 'play_music_default_volume',
        "args": [Music._21_SAD_SONG],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1104_action_queue_async_9_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1104_action_queue_async_9_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [23, 26, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1104_action_queue_async_9_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1104_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 95],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_deactivate_sound_channels_13',
        "command": 'deactivate_sound_channels',
        "args": [[0, 1, 2, 3]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1104_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
