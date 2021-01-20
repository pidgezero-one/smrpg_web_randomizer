from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1815_pause_0',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 65535, 'EVENT_1815_add_short_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_add_short_2',
        "command": 'add_short',
        "args": [0x7024, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_add_short_3',
        "command": 'add_short',
        "args": [0x7026, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_jmp_if_var_not_equals_short_4',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 10, 'EVENT_1815_set_7000_to_object_coord_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._147_CLICK, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_set_short_6',
        "command": 'set_short',
        "args": [0x7026, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_set_7000_to_object_coord_7',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1815_fade_out_music_to_volume_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_jmp_if_bit_clear_9',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 1, 'EVENT_1815_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_set_7000_to_object_coord_10',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_mem_compare_11',
        "command": 'mem_compare',
        "args": [0x7000, 1536],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_jmp_if_comparison_result_is_greater_or_equal_12',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1815_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_fade_out_music_to_volume_13',
        "command": 'fade_out_music_to_volume',
        "args": [2, 127],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_run_event_at_return_14',
        "command": 'run_event_at_return',
        "args": [1817],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1815_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
