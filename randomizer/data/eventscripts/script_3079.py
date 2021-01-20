from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3079_move_script_to_main_thread_0',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7076, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_set_bit_2',
        "command": 'set_bit',
        "args": [0x707c, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_set_bit_3_3',
        "command": 'set_bit_3',
        "args": [0x1d8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7064, 4, 'EVENT_3079_enable_controls_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_run_levelup_bonus_sequence_5',
        "command": 'run_levelup_bonus_sequence',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_enable_controls_7',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3079_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
