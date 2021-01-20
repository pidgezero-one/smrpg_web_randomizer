from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2428_run_event_as_subroutine_0',
        "command": 'run_event_as_subroutine',
        "args": [3588],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7091, 2, 'EVENT_2428_jmp_if_bit_clear_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 690],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7047, 0, 'EVENT_2428_fade_in_from_black_async_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2428_action_queue_async_4_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2428_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_freeze_camera_6',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_set_action_script_async_7',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 482],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_set_action_script_async_8',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2428_unfreeze_camera_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7091, 2, 'EVENT_2428_unfreeze_camera_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_pause_11',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_unfreeze_camera_12',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_2428_jmp_if_bit_clear_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_fade_in_from_black_async_14',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_jmp_if_bit_clear_15',
        "command": 'jmp_if_bit_clear',
        "args": [0x7099, 7, 'EVENT_2428_clear_bit_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7091, 2, 'EVENT_2428_clear_bit_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._149_CASINO_SECRET_PASSAGE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7099, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2428_ret_20',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
