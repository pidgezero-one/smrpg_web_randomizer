from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1864_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1864_ret_10']
    },
    {
        "identifier": 'EVENT_1864_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1864_run_dialog_2',
        "command": 'run_dialog',
        "args": [1252, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1864_jmp_if_dialog_option_b_3',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1864_action_queue_sync_5']
    },
    {
        "identifier": 'EVENT_1864_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1864_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1864_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1864_slow_down_music_6',
        "command": 'slow_down_music'
    },
    {
        "identifier": 'EVENT_1864_pause_7',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_1864_fade_out_to_black_async_duration_8',
        "command": 'fade_out_to_black_async_duration',
        "args": [40]
    },
    {
        "identifier": 'EVENT_1864_jmp_to_event_9',
        "command": 'jmp_to_event',
        "args": [3356]
    },
    {
        "identifier": 'EVENT_1864_ret_10',
        "command": 'ret'
    }
]
