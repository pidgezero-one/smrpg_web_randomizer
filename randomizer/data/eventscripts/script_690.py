from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_690_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 65, 'EVENT_690_fade_out_music_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_run_dialog_2',
        "command": 'run_dialog',
        "args": [2114, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 7, 'EVENT_687_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_fade_out_music_5',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_690_action_queue_async_6_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_690_play_music_default_volume_7',
        "command": 'play_music_default_volume',
        "args": [Music._49_CELEBRATIONAL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_pause_8',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_run_dialog_9',
        "command": 'run_dialog',
        "args": [2331, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_pause_10',
        "command": 'pause',
        "args": [170],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_run_dialog_11',
        "command": 'run_dialog',
        "args": [2332, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_pause_12',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_run_dialog_13',
        "command": 'run_dialog',
        "args": [2333, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_pause_14',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_play_music_default_volume_15',
        "command": 'play_music_default_volume',
        "args": [Music._39_MARRYMORE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_690_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
