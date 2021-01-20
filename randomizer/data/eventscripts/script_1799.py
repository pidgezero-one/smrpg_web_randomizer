from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1799_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_set_short_1',
        "command": 'set_short',
        "args": [0x7034, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_set_7010_to_object_xyz_2',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_start_loop_n_times_3',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_pause_4',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_create_packet_at_7010_coords_jmp_if_null_5',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1799_pause_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_pause_6',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_add_short_7',
        "command": 'add_short',
        "args": [0x7034, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_end_loop_8',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_remove_from_current_level_9',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 7, 'EVENT_1799_run_dialog_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_run_dialog_11',
        "command": 'run_dialog',
        "args": [1238, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_ret_12',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_run_dialog_13',
        "command": 'run_dialog',
        "args": [1230, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1799_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
